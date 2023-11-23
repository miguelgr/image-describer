# FREEPIK Image Describer

## Introduction

A system to infer image titles using an ML model.

### Requirements

Functional Requirements:

- Infer an image title through an API request, using the `microsoft/git-base-textcaps` model.

    `predict_image_title `

Non Functional Requirements:

- Highly Performant: expected to perform under load and volume.

- Fault Tolerant: tolerate mistakes or sw. exceptions.

- Highly Scalable: handles growth.

### System Design Solution

![simple design](static/simple-design.png)

A simpler solution,  more naive but yet functional is a system composed of load balancer in front of the service nodes, which run the API in an async manner and use queues to create tasks for requesting image titles to a pool of processes and get the inference results in a request/response cycle.

Sticky round-robin or dynamic load balancing algorithms to serve the requests based on the CPU usage of the services could improve performance and availability

This approach can scale vertically and horizontally. Adding more powerfull machines and/or nodes during traffic peaks means the processing capability is extended, but yet there is a drawback, the API and the processing are coupled and can't scale separately.

A better solution where these two services are decoupled is desired.

### API

### Worker

## Usage

`docker-compose build` and  `docker-compose  run`
