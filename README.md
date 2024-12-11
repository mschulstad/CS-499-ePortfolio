# CS-499-ePortfolio 


## Self-Assessment
Completing my coursework and developing my ePortfolio throughout the Computer Science program has been an invaluable process for highlighting my strengths and growth as a developer. The ePortfolio showcases a curated selection of projects that demonstrate my technical proficiency, analytical thinking, and problem-solving abilities. By applying core computer science principles across diverse assignments and challenges, I have built a solid foundation for a successful career while creating a portfolio that effectively communicates my expertise and adaptability to potential employers.
Throughout my time at SNHU, I have developed a diverse set of technical and professional skills. Several projects required me to collaborate effectively with stakeholders and users, translating their needs and requirements into detailed design documents and functional code. These experiences refined my ability to communicate clearly and adapt solutions to meet real-world challenges. I also deepened my understanding of security in software development by writing unit tests to identify and address potential vulnerabilities, ensuring the integrity and reliability of my applications. My portfolio further demonstrates my expertise in essential areas such as data structures and algorithms, software engineering principles, and database design, showcasing my ability to create scalable, efficient, and user-focused solutions. Each project reflects my commitment to learning and applying these concepts in innovative ways.

## Summary
The portfolio shows the original version of a text based game written in python and an updated text based game. In the text-based game, players navigate a spaceship by moving from room to room, with the goal of collecting all available items while avoiding the ghost. The game ends either when all items are collected, marking a victory, or when the player encounters the ghost, resulting in a loss. In the updated version, the gameplay has been enhanced to increase complexity and engagement. The ghost now moves dynamically around the spaceship, creating a more challenging and unpredictable experience that requires strategic decision-making from the player. Additionally, a save-and-load feature has been implemented, allowing players to save their progress at any point and resume the game later. This improvement not only enhances user experience by providing flexibility but also showcases advanced programming skills in file handling and state management. These updates make the game more interactive, immersive, and user-friendly. there were small challenges faced when updating the code, no major or code breaking errors. In the original code the user input was handled so it didn't matter the about the case it was input as but when updating the code the user input was handling that correctly and the items in rooms weren't being shown on output. So if the user entered go north it didn't work but go North did and the user never knew when an item could be collected so unless they always input collect item when entering a new item they wouldn't be able to finish the game. I feel like software engineering and databases are fully met while algorithms and data structures are only partially met. initially for algorithms and data structures I wanted to have some rooms require a puzzle to exit the room, in addition to have the ghost move rooms, but I wasnt able to complete the puzzles and get the puzzles to be how I wanted them. the puzzle idea I had didnt translate great to a text based game. 

## code review 

the code review is a review of two artifacts. A zipped file of it is posted in the ePortfolio

## Narratives 

#### Software Design and Engineering
The game was redesigned using object-oriented programming principles to enhance scalability and maintainability. The Room class was introduced to encapsulate room-related data, such as exits and tools, and the Game class manages the game's overall functionality, including player movement, tool collection, and villain behavior. This structure not only reduces redundancy but also makes the codebase easier to expand with new features, such as additional rooms, tools, or mechanics. Clear separation of concerns allows for better modularity and testing of individual components.
I selected this project because when i was first making it I thought of ways to further improve the game and additionally it was the first project i worked on at SNHU so I thought it would be a good way to show growth. The refactored code, particularly the Room and Game classes, showcases object-oriented design principles, modularity, and separation of concerns. These components demonstrate the ability to structure complex systems in a maintainable and scalable way. By encapsulating room and game-related logic into dedicated classes, the enhancement streamlined the code, reduced redundancy, and made it easier to expand. This refactoring also improved readability and maintainability, which are essential for larger projects. The enhancement highlighted skills in object-oriented programming, including class design, inheritance, and encapsulation. It also demonstrated proficiency in refactoring code for clarity and scalability while adhering to coding best practices.

#### Algorithms and Data Structure
The game's logic was improved by introducing a dynamic villain behavior, where the villain moves randomly to a connected room whenever the player moves. This enhancement adds complexity and unpredictability to the gameplay, requiring efficient handling of connected room relationships. The room connections are implemented using dictionaries for fast lookup, and random selection ensures that the villain's behavior is unpredictable yet computationally efficient. These changes leverage basic graph traversal concepts to add depth to the game.
I selected this project because when i was first making it I thought of ways to further improve the game and additionally it was the first project i worked on at SNHU so I thought it would be a good way to show growth. The refactored code, particularly the Room and Game classes, showcases object-oriented design principles, modularity, and separation of concerns. These components demonstrate the ability to structure complex systems in a maintainable and scalable way. By encapsulating room and game-related logic into dedicated classes, the enhancement streamlined the code, reduced redundancy, and made it easier to expand. This refactoring also improved readability and maintainability, which are essential for larger projects. The enhancement highlighted skills in object-oriented programming, including class design, inheritance, and encapsulation. It also demonstrated proficiency in refactoring code for clarity and scalability while adhering to coding best practices.

#### Databases
A save and load feature was added, allowing players to preserve and resume their game progress. This was achieved by using JSON serialization to store the game's state, including the player's current room, inventory, and the villain's location. The implementation of this feature introduces database-like functionality, ensuring data persistence across sessions. While lightweight, this approach simulates fundamental database operations, such as saving and retrieving structured data, making it a practical demonstration of data management in game development.
I selected this project because when I was first making it I thought of ways to further improve the game and additionally it was the first project i worked on at SNHU so I thought it would be a good way to show growth. The save and load functionality showcases the ability to manage data persistence using JSON. This feature required designing a system to serialize and deserialize the game state effectively. The addition of save and load capabilities made the game more user-friendly by allowing players to pause and resume their progress. This improvement aligns the game with modern gaming standards, enhancing its usability and appeal. The enhancement demonstrated skills in data serialization, file I/O operations, and structured data management using JSON. It also showcased the ability to integrate persistent data storage into an interactive application, simulating basic database functionality.
