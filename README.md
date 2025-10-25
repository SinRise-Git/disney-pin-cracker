# Disney Pin Cracker 
A Python script to try all 10,000 codes for a Disney+ account until it finds the right one

## Argparses 
* **-a**: Authorization Token:
  While logged into Disney+ on [www.disneyplus.com](https://www.disneyplus.com), open your browser’s developer tools, go to the **Console** tab, and run the following JavaScript snippet to retrieve your authorization token from localStorage:
  ```javascript
  console.log(JSON.parse(localStorage.getItem('__bam_sdk_access--disney-svod-3d9324fc_prod')).context.token);
  ```
* **-p**: Profile ID:
  Navigate to the Disney+ profile you want to brute force. The profile ID is part of the URL in the PIN entry page:
  `https://www.disneyplus.com/en-gb/enter-pin/XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX`
  Copy the **XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX** portion as the profile ID.

## Setup

## 1. Clone the repository
```bash
git clone https://github.com/SinRise-Git/disney-pin-cracker.git
```
## 2. Move to the repository 
```bash
cd disney-pin-cracker
```
## 3. Create a venv for the packages (Optional)
Creating a virtual environment (venv) is optional but recommended.
```bash
python -m venv venv
```
## 4. Start venv (Skip if you didn't create a venv)
**Windows**
```bash
venv\Scripts\activate
```
**Linux**
```bash
source myenv/bin/activate
```
## 5. Downlaod required packages 
```bash 
pip install -r requirements.txt
```
## 6. Run script
```bash 
python main.py -a YOUR_ AUTHORIZATION_TOKEN -P PROFILE_ID
```

