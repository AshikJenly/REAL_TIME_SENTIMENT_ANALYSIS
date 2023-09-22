package com.home.front.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class KafkaController {

    private final KafkaTemplate<String, String> kafkaTemplate;
    private final String kafkaTopic;  // Replace with your Kafka topic name

    @Autowired
    public KafkaController(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
        this.kafkaTopic = "orders";  // Replace with your Kafka topic name
    }

    @GetMapping("/api/kafka/send")
    public String sendMessageToKafka(@RequestParam String message) {

        System.out.println("\n-----------------------------------\n");
        System.out.println(message);
        System.out.println("\n-----------------------------------\n");

        kafkaTemplate.send(kafkaTopic, message);
        return "Message sent to Kafka: " + message;
    }
}
