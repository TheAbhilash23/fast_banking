# Banking Application - Event-Driven Microservice Architecture on FastAPI

This is a modern banking application designed using event-driven microservices. The architecture leverages Apache Kafka (KRaft mode) for service communication and data streaming. This application is built for scalability, high availability, and real-time processing, with dedicated services for handling customers, payments, transactions, and more.

## Table of Contents

- [Architecture Overview](#architecture-overview)
- [Services](#services)
- [Development Setup](#development-setup)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Development Scripts](#development-scripts)
- [Contributing](#contributing)
- [License](#license)

## Architecture Overview

This banking application consists of multiple microservices communicating asynchronously via Apache Kafka in KRaft mode (no external Zookeeper dependency). Each microservice is responsible for a specific domain in the banking system, and Kafka topics are used to stream, process, and relay events across services.

### Event-Driven Services:

- **Analytics Service**: Collects and processes real-time banking metrics.
- **Customers Service**: Manages customer information, registration, and updates.
- **IAM Service**: Handles identity and access management.
- **Payments Service**: Processes all payment-related actions.
- **Products Service**: Manages bank products like loans, accounts, and cards.
- **Transactions Service**: Handles database transactions between accounts.

## Kafka Integration

Kafka is the backbone of the event-driven architecture used for message streaming between services. This project uses **KRaft mode**, enabling Kafka to run without the need for an external Zookeeper.

- Kafka topics are used for communication between microservices.
- Each microservice produces and consumes messages from specific Kafka topics.
- Configurations for Kafka (brokers, topics, etc.) are stored in `config/development/kafka.configuration`.

## Development Setup

### Prerequisites

- Linux OS (for running shell scripts)
- Docker & Docker Compose
- 
- Kafka (KRaft) (included in the Docker Compose setup)
- PostgreSQL or any relational database (included in the Docker Compose setup)

### Running the Application

To run the application locally, ensure you have Docker Compose installed and follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/TheAbhilash23/fast_banking.git
    cd fast_banking
    source tools/run_dev.sh
    ```
   
2. The services should now be running on your local machine.

### Database

- The default database is configured in `config/development/db`.
- Each microservice connects to its own database instance, as specified in the Docker Compose file.

## Configuration

### Kafka Configuration

Kafka configurations for development are available in `config/development/kafka`. This includes settings for brokers, topics, and producer/consumer properties.
```yaml
KAFKA_NODE_ID: 1
KAFKA_PROCESS_ROLES: broker,controller
KAFKA_LISTENERS: PLAINTEXT://fast_banking_kafka:9092,CONTROLLER://fast_banking_kafka:9093
KAFKA_CONTROLLER_LISTENER_NAMES: CONTROLLER
KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://fast_banking_kafka:9092,
KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,CONTROLLER:PLAINTEXT
KAFKA_CONTROLLER_QUORUM_VOTERS: 1@fast_banking_kafka:9093
KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR: 1
KAFKA_TRANSACTION_STATE_LOG_MIN_ISR: 1
KAFKA_MIN_INSYNC_REPLICAS: 1
KAFKA_NUM_PARTITIONS: 1
KAFKA_DEFAULT_REPLICATION_FACTOR: 1
KAFKA_LOG_RETENTION_HOURS: 168
KAFKA_LOG_SEGMENT_BYTES: 1073741824
KAFKA_MESSAGE_MAX_BYTES: 10485760
KAFKA_REPLICA_FETCH_MAX_BYTES: 10485760
KAFKA_REPLICA_FETCH_RESPONSE_MAX_BYTES: 10485760
```

### Database Configuration
for development purpose we prefer to use database schema based separation among microservices
but for production environment a separate database connection can also be preferred for certain microservices.

```yaml
POSTGRES_USER=admin
POSTGRES_PASSWORD=root
POSTGRES_DB=fast_banking
```

## Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

Fork the repo and create your branch from master.
If you've added code that should be tested, add tests.
Ensure the test suite passes.
Make sure your code follows the PEP code style guidelines.

## Licensing
This software comes under  
### GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
