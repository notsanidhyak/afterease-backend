<h1 align="center">After Ease</h1>

APIs- https://documenter.getpostman.com/view/19649785/2s93JqRjeF

[Idea Submission](https://docs.google.com/presentation/d/1kOnasO5t7KhjDZZ77dV6p12BacTB1_Sg/edit#slide=id.p1)

website Live at- https://after-ease.netlify.app/  
demo video- https://youtu.be/8rsyRUIYIzg

## Development 🔧

## Setup

PS- We are using a free tier of twilio to send APIs and the dummy database of adhaar, CPAO and other documents and it sends to only twilio verified phone number for a particular account. So you can contact mugdhasharma0327@gmail.com if you wish to take a demo of website.


```sh
$ git clone https://github.com/AfterEase/afterease-backend.git
$ cd afterease-backend
```

### For setting virtual environment

```sh
$ virtualenv venv
```

### For activating virtual environment in Windows

```sh
$ venv/Scripts/activate
```

### For activating virtual environment in Linux and macOS

```sh
$ source venv/bin/activate
```

### For deactivating virtual environment
```sh
$ deactivate
```
After creating virtual environment

### Start

```sh
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

### Problem we are trying to solve- Loophole in gov process.

- Currently all the processes of birth certificate, Adhaar, PAN card, death certificate, voter ID generation have been digitised by the government but only few of them have been linked. This raises the possibility  of problems like the development of fake identities, the use of papers by criminals for illicit actions after a person's death, the casting of bogus votes in elections, and the acquisition of fake SIM cards by terrorists using fake identities. Even when a person passes away, their family members have to manually dissolve these documents by visiting to several offices.

- Recovery of excess pension given to deceased person who passes away before the deadline of submitting proof of life is also a big headache for government. the value of money may change over time, and recovery of the excess amount from the legal heirs may take a long time, depending on various factors such as the legal system, documentation, and other formalities. Even if value of rupee changes by ₹3-5, still on a large scale it is a big financial loss for government.

- Ultimately, despite the fact that these documents are highly dependent on one another, yet there are no links or automated triggers for the necessary activities. Thinking about the scenario where in near future all of the identity documents will be linked to each other, we can use this link to solve major issues efficiently, the management of a person’s digital identity would become easier

### Solution we propose-
Our web portal will be an extension to the already existing government portals which generate death 
certificates:  
● If the deceased person was eligible for government pension, we will automatically trigger the process to stop or change the pension during the death certificate generation according to the applicable policy. This will prevent any misuse of government funds that come from taxpayers' wallets.Other functionality we’ll offer on our web portal are as follows:  
● Family member of the deceased will need to authenticate using an Adhaar-based OTP mechanism on our portal. Upon authentication, assuming the pre-existing government portal has generated the death certificate using the family member's input, we'll have access to the unique ID from the death certificate. Next, they will be presented with the following options:  
○ Identity Theft solution: This option will automatically initiate the process to deactivate or delete the deceased person's Aadhaar, PAN, and Voter ID. This feature helps to prevent identity theft and misuse of the deceased person's documents.  
○ Bank account transfer solution: This feature triggers the process of transferring the deceased person's registered bank account to the nominee of the account. This simplifies the process of accessing funds and ensures that the funds are received by the right person without any hassle.  
● As a separate feature, we’ll also provide automatic notifications to users once they turn 18 regarding their voter ID and PAN making process. This ensures that the user is informed about the necessary steps required to complete the process.  



