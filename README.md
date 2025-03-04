<h1 align="center">
Spe* Generation System
<h1/>


<p align="center">
    <img src="page/Spe.png" width="1080" alt="CHIFEngine logo">
</p>


###  Spe* is a modular and scalable Entity & World Generation System designed for Project Voronoid and large-scale-procedural games. It provides procedural generation, a custom binary storage format and an ECS-based architecture for high performance. 

## Introduction

Spe* is built with the intention of providing a high-performance, procedurally generated world system that scales for large-scale open-world games. Its core focus is on performance and flexibility, allowing for dynamic world creation, vast NPC systems, seamless terrain generation, and more.

This system leverages Entity-Component Systems (ECS) to keep the game's world and entities highly modular, reducing coupling and making it easier to develop complex systems without sacrificing performance. The custom binary storage format allows for fast loading times and a lightweight footprint, ensuring the game runs smoothly even with vast amounts of generated data.

## Features

 - Procedural Generation: Spe* supports robust procedural world generation, enabling the creation of massive, varied game worlds without the need for manual design.
 - Modular Entity-Component System (ECS): Each game entity is made up of components (such as position, velocity, health, etc.), making it easy to add new features and behaviors dynamically.
 - Custom Binary Storage Format: Spe* uses a custom binary storage format to efficiently serialize and store world data, which drastically improves load times and data management.
 - NPC Generation: Generate NPCs with varying behaviors, attributes, and roles based on world context and player interactions.
 - Scalability: Built to scale with large game worlds, ensuring performance is maintained regardless of the world size or number of entities.
 - Cross-Platform Compatibility: Designed to work on multiple platforms, making it a versatile tool for game developers.



## Building

### Clone the repository:

```
git clone https://github.com/LL-Program/spex.git
cd spex
```

### Build the project:
```
mkdir build
cd build
cmake --
make
```

After successful compilation, you can link Spe* to your game project or test it directly by running the example worlds.

## Core Concepts
### Entity-Component System (ECS)

Spe* uses the Entity-Component System to separate concerns and maximize flexibility. The ECS architecture allows for easy composition of behavior and state by attaching components to entities, which are then processed by systems.

 - Entity: An individual object in the world (e.g., NPCs, terrain features).
 - Component: Data associated with an entity (e.g., position, health, AI behaviors).
 - System: Logic that acts on entities with specific components (e.g., a movement system that updates entities with position and velocity components).

### World Generation

Spe* provides procedural world generation through customizable algorithms. You can configure parameters like world size, terrain features (e.g., mountains, oceans), weather, and more.

 - World generation can be random or guided, depending on your needs.
 - The system allows for endless procedural generation, so you can create large worlds that expand infinitely.
 - Integration with ECS enables entities and world features to interact seamlessly.

### Custom Storage Format

To ensure performance, Spe* utilizes a custom binary format for saving and loading world data. This format is optimized for quick reads and writes, reducing load times and memory usage.

 - The storage format supports incremental saving, so only changed or new data is written, making it efficient even for large worlds.
 - Built-in utilities allow easy serialization and deserialization of world states, so you can pause and resume gameplay or save progress without impacting performance.


## Contributing

We welcome contributions to Spe*! If you'd like to contribute:

 - Fork the repository and create your feature branch (git checkout -b feature/my-feature).
 - Commit your changes (git commit -am 'Add new feature').
 - Push to the branch (git push origin feature/my-feature).
 - Create a new pull request.

Please ensure your code follows the project’s [coding guidelines](docs/SpexGeneralCodeGuidelinesEN.md) and includes appropriate tests for any new functionality.

## License

Spe* is open-source and released under the MIT License. See the LICENSE file for more details.
