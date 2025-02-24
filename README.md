##Inspiration
In a world where many popular messaging apps claim to offer the best data privacy but often fall short, our project aims to revolutionize secure communication by developing a web application that uses Morse code for interactions. This approach not only provides an additional layer of encryption but ensures that data is deeply protected. Our platform enables individuals within a network to share ideas securely, ensuring that no unauthorized person can access the data, offering unparalleled privacy and peace of mind.

##What it does
The system is built with a Raspberry Pi connected to three buttons. The first button is used to start and end a message, the second button represents the dash character in Morse code, and the third button represents the dot character. Once the Raspberry Pi is turned on, it automatically launches a website where users can easily enter and send their secret Morse code messages.

How we built it
The web application runs on the Flask framework, and I utilized MongoDB to store the data entered by each user. Each user is assigned a unique User ID with distinct colors, making it easy to identify the sender of each message.

Challenges we ran into
Flask is usually not that strong when running a website, so there were associated challenges. Initially, I utilized the session ID to uniquely identify a user, but users often got disconnected, which required me to store the user information as a cookie so my application could retrieve it when the user visits the website.

Accomplishments that we're proud of
Initially, I felt that the scope of this project was realistic because building such a secret messaging app required multiple layers. I had to establish the principles and ideas behind the security I wanted my application to solve. I built the website and decided on various features to make it user-friendly, and also found a way to uniquely identify each user.

What we learned
This was the first time I used MongoDB, as well as creating a web application based on security principles. However, the most important lesson I learned was about sockets and how they enable communication across a network.

What's next for MorseApp
Currently, the cost of building MorseApp is $90, primarily due to the $85 Raspberry Pi and additional components like buttons and wires. However, by replacing the Raspberry Pi with an $8 ESP32 and also investing in a small LCD screen, I believe we can reduce the cost to $30. These improvements would allow us to create a product the size of a watch that can securely send messages across a network.