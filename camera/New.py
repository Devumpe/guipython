config = {
    "apiKey": "AIzaSyB_jnpsPaxKs3xEhs-AbknZJXjcK-M4IeU",
    "authDomain": "water-meter-235712.firebaseapp.com",
    "databaseURL": "https://water-meter-235712.firebaseio.com",
    "projectId": "water-meter-235712",
    "storageBucket": "water-meter-235712.appspot.com",
    "messagingSenderId": "67042893322"   
}

#อัพไฟล์ database
    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    timeStamp = time.strftime("%Y-%m-%d:%H-%M-%S")

    db.child("room").push({"image": {"rfid":"12","url": blob.public_url,"date": timeStamp}})
except Exception as e:
    print("e")
