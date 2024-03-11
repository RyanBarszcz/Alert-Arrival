Inspiration:

Have you ever found yourself battling drowsiness while driving, unable to keep yourself fully awake? If you said yes, you are not alone. There are over 300,000 police-reported crashes each year that are due to drowsy driving.

Drowsy driving is a serious and life-threatening issue that severely hinders the overall safety of civilians each day. The psychological and physiological repercussions of drowsy driving is comparable to driving under the influence of alcohol or drugs. Low-income individuals still lack accessibility to natively integrated systems, hence the need for additional support with the detection and prevention of drowsy driving within the automotive industry.

Alert Arrival was built to enhance road safety by serving as an embedded system specifically designed for integration into motor vehicles. The driving force behind this project was to detect and prevent incidents related to driver drowsiness, therefore mitigating the risks associated with fatigue-related accidents.

What it does:

Alert Arrival is a software solution that prioritizes the safety of drivers and civilians through computer vision, generative AI, and various software components. When drowsiness is detected through our computer vision framework, our generative AI voice assistant promptly engages in conversation with the at-risk user in order to prevent drowsy-driving related incidents and ensure their safety.

How we built it:

Our project is comprised of three main components: computer vision, the application itself, and generative AI. The computer vision software component was created using python and utilized the opencv and dlib libraries. With these libraries, we were able to successfully access the native webcam within one of our local machines and produce a script that calculated the eye aspect ratio (EAR) and detected eye closures. Once a certain threshold was met in terms of duration closed, this would then write to firebase and trigger our accompanying software. The software application itself was built using flutter, dart, and firebase in Android Studio to interface with the user directly. Our final component, the Generative AI Voice Assistant, was an open-sourced framework titled "Alan AI" which we tuned to our specific needs as a drowsy-driving detection and prevention system. This voice assistant was compiled using javascript and flutter. To link all of these components, we utilized firebase as a Realtime Database on the backend.

Challenges we ran into:

Originally, we wanted to create a hardware and software-based solution utilizing a Raspberry Pi4 and camera module to directly emulate our innovative system. This ambitious idea was put on hold due to several networking restrictions, such as firewall configurations that prevented SSH and Virtual Network Computing. Fortunately, we were still able to implement the desired functionality of the original hardware assembly through the native webcam of one of our devices.

Accomplishments that we're proud of:

We are proud of our effective collaboration and the delegation of tasks that led to the production of a functioning application. Having a finished product with the functionality that we intended is a tremendous milestone, and we are more than pleased with what we were able to produce by the completion of the event. We feel as though we maximized the potential of the project by playing to our individual strengths throughout the development process.

What we learned:

This project provided a well-rounded introduction to several topics within computer science and software engineering. Neither of us had previously worked with flutter or dart in a programming environment and found these to be exciting and beneficial to the overall infrastructure of Alert Arrival. In addition to this, Generative AI is something we both were familiar with but had never directly implemented or trained as a functional component of an application. This new avenue is something we both agree will be beneficial to our future careers, seeing as AI/ML is an emerging field particularly within the automotive sector.

What's next for Alert Arrival:

Alert Arrival will be fully integrated within various vehicle systems in the near future. This detection software will not only utilize eye closures, but also line-following AI to detect lane departures and additional biometric inputs such as touch intensity with the steering wheel. We aim to implement vibration in seating components to contribute to alertness, as well as auditory cues and haptic feedback to engage the driver while in the drowsy-driving mode. This is an application that we would also love to see involved in the automotive subsector of motorsports, such as endurance racing (WEC) to ensure the safety and alertness of drivers and spectators in real-time.
