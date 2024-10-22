# Tiered P2P Communication and Database System
This project was completed as part of a computer networks module in third year. In brief it involved the creation of a distributed peer to peer communication and database system 
to be used for the recording and discovery of missing persons during the widespread displacement of people following the Rohingya acrisis in Myanmar.
A full description is available in the project report below. 

### A brief summary of Project 2 knowledge and experience
 Before Project 2, we had only read about P2P applications and basic Client-Server socket program
ming in the course book. Therefore it was a challenging project with tons of takeaways. We watched a
 lot of videos and browsed the web for information and we gained knowledge and experience in socket
 programming. Both groups were able to make a reasonable implementation of a decentralized P2P
 network framework for Project 2, “reasonable” when considering the time we had and prior knowledge
 and experience on the subject.
 We have learned that implementing a P2P network is a challenging task. We understand that there
 are many things to consider when designing a P2P framework, e.g. how nodes should connect to each
 other, which protocols to use, data synchronization, reliability and security. We have recognised the
 need for a decentralized network in conflict zones, where a decentralized network can continue to op
erate even if some nodes are offline or shut down. In Project 2 we learned by doing, which is arguably
 the best way to learn. This project allowed us to gain a better understanding of P2P networks and
 we got practical experience of using TCP and UDP in code. We got to know how to use multiple
 threads so each peer in our implementation can act as a server and a client at any given point in time.
 We learned how to implement database access control by using mutexes for synchronization. We also
 gained more experience in using git and GitHub for version control which is really practical.

 ### Primary focus
 For this project, our primary focus is the oppression faced by the Rohingya muslims of Myanmar.
 The Burmese military government has, for the past several years, clamped down on this minority
 group, attacking and raiding villages populated by them. Naturally, this has led to Myanmar being an
 active conflict zone, and as is expected from such crises, the physical and emotional distress caused to
 people of the Rohingya community has been immeasurable. The constant oppression has resulted in
 people trying to seek refuge in neighbouring countries, leaving families and communities fragmented
 or dismembered. In such situations, a reliable line of communication between and among civilians and
 hospitals/refugee camps is vital. Moreover, affected individuals/groups should be able to view missing
 person or patient records put up by trusted organisations in order to expedite the reunification of
 families (or at the very least, ensure transparency). One of the major hindrances to this is the
 centralised, easily collapsible nature of networks in such locations. It is imperative for a consistent
 data fabric to be devised- one that doesn’t depend on a single central server for its functioning. This
 is where P2P networks come in.

 ### Networking/Communication aspects of our solution
 We aim to help with issue this by implementing a peer to peer network within which identity authen
ticated trusted nodes, will be capable of sending messages and altering and sharing a decentralised
 database containing information on missing, found and deceased persons, vaccine records, refugee camp
 censuses etc. This network will operate in a tiered hierarchy with Tier 1, consisting of trusted nodes
 ran on AID group devices, all of which have are capable of communicating on a peer-to-peer basis and
 altering the information contained within the shared database. Tier 2 will consist of refugee’s edge
 devices who will only have permission to view certain non-sensitive information within the database
 and who communicate with the collective tier 1 through a client server relationship.
 

Each trusted node will be assigned a twelve-digit token generated on acceptance into the network
 and this will be used to authenticate their identity before any inter node communication takes places.
 To prevent potential leaks of these authentication tokens, user will be unaware of their own and other
 peers tokens and only know the simple peer numbers e.g. 1, 2 ,3, 4, of the other nodes in the network.
 Every node will run an always on listening server in a separate thread which will be ready to
 accept pings from other peers who wish to establish a connection. For example when Node A wishes
 to communicate with Node B, A will send it’s token via a UDP client socket to B’s listening server.
 B will then check this token against its list of trusted peers. If the peer is trusted then B will create a
 new thread and open a TCP server on this Thread before opening UDP client socket which will send
 the Port number of this newly established TCP server socket to the listening port of A.

 A will then create a new thread, establish a TCP client socket on it and using the port number it
 just received, make a handshake with the TCP socket of B. All network functions carried out by the
 node will be conducted through these TCP sockets, for example sending text messages, broadcasting
 emergency alarms to all known peers, transferring files individually and broadcasting file updates to
 all known peers when the database has been updated locally in order to maintain file version control.
 Each node also has the ability to sustain multiple parallel TCP connections simultaneously through
 the use of multithreading. Whenever a new trusted peer makes contact the listening server will auto
matically create a new thread, preventing it from being blocked by one specific connection, freeing up
 the main thread to deal with user inputs/programme outputs and theoretically allowing the ability to
 maintain as many parallel connections as the device can sustain. Mutexes are also used in conjunction
 with multithreading, locking the database on each node when in use, to prevent a situation where
 multiple file updates were sent simultaneously resulting in only one being received.

 Tier 2 devices can only view their local database version or make request for a refresh from Tier 1.
 When this refresh request is made the tier 2 node will pick a random tier 1 peer out of its database
 of known tier one devices and send a specific code to the listening server of said device. When this
 code is received by the listening server, the tier 1 device will send an appended version of the shared
 tier 1 database with the sensitive id number field removed. If this first request is not successful, the
 tier 2 device will continue randomly polling the peers in tier 1 for a refreshed file version until one is
 received or the max number of attempts’ is reached and the user is notified with an error message.

 ### Requisite knowledge/skills necessary

 To realise our solution it is necessary to have a basic understanding of networking concepts, like
 P2P and Transport Layer protocols. It is also good to have some socket programming knowledge and
 experience in Python (or for similar languages). It is also important to understand how multi-threaded
 applications and some experience using mutexes.

 ### Our Test Cases

 Our potential test cases which we discussed in our meetings had to be relevant to how we believe our
 project would be used practically in a conflict zone. With this in mind we decided that our first test
 cases would be the same test cases that were used in Joe and Colm’s project 2. These were to send
 a message to another peer, send the database to another peer and add an entry to our database. We
 already had these working so we had to add some more test cases. We decided that we wanted to
 add the ability to send an alarm message to all peers on the network and then manually send a peers
 database to all peers on the network. The reason why we added these was we wanted to be able to
send an alarm message in case of an incident/attacks on a refugee site so that other peers could inform
 refugees camps about this. We also wanted the ability to manually update the databases of other peers
 because internet connection is not going to be guaranteed in any conflict zone.
 Project plan, management and execution

 The group met as soon as possible after receiving information about group members for Project 3 and
 we started discussing the scope of the project. Our Project 2 groups were working on similar concepts
 in a way, Joe and Colm were making a secure P2P database and messaging network to provide aid
 in the Rohingya conflict ongoing in Myanmar and Hafsteinn and Aniket were making a P2P network
 framework for hospital communication in conflict zones. Hafsteinn and Aniket had parallel connections
 while Joe and Colm had a token based peer authentication and a functioning database and we wanted
 to integrate those elements in our implementation for Project 3. We decided to stick to Joe and Colm’s
 use case from Project 2. We set out to improve the implementation by allowing parallel connections
 between nodes, adding database access control with mutex locks and dedicating each peer to a certain
 organization in Myanmar and its surroundings. We wanted to make those improvements because we
 think they are useful to making our network service more beneficial to the people who would be using it.
 We met often during the project lifetime and decided what each person was responsible for work
ing on between meetings. During meetings we also went over what was going well and discussed
 problems and challenges. We divided tasks based on each individual’s strengths. The first thing we
 aimed for was to get connected to the Raspberry Pi computers and get some implementation running
 on them. That went well and we spent a lot of time together in the LG12 laboratory where we worked
 on our implementation and conducted testing

 ### Groupwork challenges and issues managed

 Wecame across some challenges with the code during the project. By debugging the code we were able
 to fix the problems (many minor problems to start with like not having the right IP address values in
 the token file). There was also a challenge to decide on a solution for sharing databases between nodes,
 that is how we were going to replicate data over the nodes in the network. We dealt with challenges like
 that by discussing possible solutions, brainstorming together and by dividing responsibilities between
 meetings. Our main issue came up on the day of our demonstration when we had been working
 on different things in different branches in git and we got merge conflicts when merging the changes
 together. We had tested individual changes to the implementation on the Raspberry Pi computers with
 good results. However we were not able to resolve those merge conflicts in time for the demonstration so
 we found a version that worked properly and had already been tested on the Raspberry Pi computers
 and used that for our demonstration. Looking back we should have accepted to implement fewer
 features and merge them earlier on for final testing, but we were too focused on adding all the features
 we set out to implement and time got us in the end.
 Validation of test cases and implementation

 To validate our implementation we used tests to see if our system was working as we intended. We
 had to validate our functions and for the Raspberry Pi computers we had to validate that everything
was set up properly according to their IP-addresses. We tested that all peers were able to connect
 to each other and were also able to send/receive files and messages. We had to test the SOS alarm
 functionality and if parallel connections worked properly. We tested the database access control with
 mutexes and the broadcast functionality, which sends a updated database from one peer to all other
 peers in the network.

 We were able to get all of these tests cases working eventually. Implementing the alarm test case
 was difficult as it required us to be able to message all peers at once which caused issues but we
 handled those issues. After testing and implementing the SOS alarm functionality it was less complex
 for us to test and implement our broadcast functionality as it works very similarly to the alarm func
tionality.

 That was how our functions were tested and implemented but we also had some other tests we wanted
 to run. We wanted to be able to disconnect a peer from the network and show that the peer will try to
 connect to other peers and have it time out due to a lack of response over a ”reasonable” time period.

 ### Reflection of Project

 We believe that our solution in its current state has no real world viability. There are multiple reasons
 for us to say this however the biggest being the inability of discovering new peers on the network.
 However, we do believe that the program could be improved upon to make it more viable. We say
 this as if a discovery system were to be implemented, it could make first time connection into the
 network very straightforward and it would improve project quite a bit. We believe that our solution
 &implementation of our networking and of our project was met the requirements of the project brief.
 Possible Improvements on the Proposed Model (xiii.)
 There is scope for improvements to the model in several aspects, mostly when it comes to end-to-end
 encryption, maintaining data integrity, and improving connectivity. These problems can be addressed
 in future versions by the following methods:

 • Encryption using TLS: Transport Layer Security can be added to our model for a greater level of
 message/file security. At the lowest level, TLS provides encryption of the data transmitted between
 the two parties. This encryption is achieved through the use of symmetric encryption algorithms,
 such as AES or 3DES.
 In addition to encryption, TLS also provides message authentication and integrity checking. This is
 accomplished through the use of hash functions, such as SHA-256 or SHA-384. The hash function
 generates a unique message digest for each message transmitted, which is then used to verify the
 integrity of the message and to ensure that it has not been tampered with in transit.

 • Full Decentralisation of the model using Blockchain Smart contracts: In a blockchain
 network, each transaction is recorded as a block and added to a chain of blocks in a linear and
 chronological order. Once a block is added to the chain, it cannot be altered or deleted, providing
 a secure and tamper-proof record of all transactions on the network. This aligns perfectly with our
 use case- maintaining file security, as mentioned earlier, is vital. Integrating blockchain technology
 to our P2P network allows for a fully decentralised fabric, ensuring data integrity at every step. In 4
particular, a modular framework such as Hyperledger Fabric would be the best fit for our model
 as it lets developers customize the blockchain network according to their specific needs. Adding
 blockchain to this network would truly elevate it to the next level: enhancing security, increasing
 trust and improving efficiency.

 • Improving the Discovery System: As it stands, while our model allows new peers to connect, it
 doesn’t help them figure out which nodes to attempt to make a connection with. In future versions,
 we could attempt to devise a discovery system that actually facilitates the connection process for new
 peers- providing information about the peers on the network that may be relevant to the new node
 (for example, IP and port addresses of hospitals and refugee camps for greater ease of use). Peer
 verification (in order to prevent peers trying to connect with malicious intent) must also be added in
 the future. Moreover, continuous monitoring of peers by the discovery system is another quality of
 life feature that would help keep the network up to date: removing disconnected or malicious peers
 and updating peer metadata


### Folder Description:
The main project folder consists of two files, local demo, for interprocess communication on one device, and raspberry demo, for use on the remotely accessed raspery pi devices.
The only difference being the IP addresses stored in the trusted peer file.

In each Demo folder there are 3 tier 1 peer folders containing all the neccessary files to run a Tier 1 node, and 1 tier 2 folder, containing all the neccessary files to run a Tier 2 node.

In each node folder the 2 files of note are:#

p2pX.py -- This file contains the main programme to be run for each node 
DATABASEx.txt -- This file contains the database of missing persons and all relveant data fields

In the tier 2 node folder the 2 files of note are:

t2_1.py -- This file contains the main programme to be run for the t2 node 
T2DATABASE.txt -- This file contains the database of missing persons and all relveant data fields
