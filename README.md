# Kris Kringle Web App with Python
A simple web app built with Python, [Parcel](https://parceljs.org/), [Bulma](https://bulma.io/) and [Vue 3](https://v3.vuejs.org/) that can be used to help decide "who gives gifts for who" at Kris Kringle every year.

It also gives participants the ability to give hints to whoever got them 🎁

## Screenshot
![Tux, the Linux mascot](/images/kris-kringle-screenshot.png)

## How to Run
### Step 1
Install all NPM dependencies
```sh
cd frontend
npm install
```
### Step 2
Build the front-end application
```sh
npm run build
```
### Step 3
Create a Python virtual environment
```sh
cd ..
python3 -m venv venv
```
### Step 4
Step into the Python virtual environment
#### **On Mac/Bash:**
```sh
source venv/bin/activate
```
#### **On Windows (Command Prompt):**
```sh
source venv/Scripts/activate.bat
```
#### **On Windows (PowerShell):**
```sh
source venv/Scripts/activate.ps1
```
### Step 5
Install required Python dependencies
```sh
pip install -r requirements.txt
```
### Step 6
Start the web server:
```sh
cd api
python KrisKringle.py
```

## Creating a Dataset
In order for this app to have a use, we need to create a dataset which involves listing all participants (people involved in the Kris Kringle) and assigning them a **recipient** - who they need to buy a 🎁 for.

To do this, create a new terminal window, repeat Step 4 and run `python create_dataset.py Name1 Name2 Name3 Name4`.

For example, if Dom, John, Pete and Vanessa are involved in Kris Kringle, run this:
```sh
python create_dataset.py Dom John Pete Vanessa
```
If successful, you should see a list of URLs which each person needs to go to in order to access the application (and see their recipient).