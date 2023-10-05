package com.home.front.controller;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.home.front.common.SingleTweet;

@Controller
@RequestMapping("/api")
public class KafkaController {

    private final KafkaTemplate<String, String> kafkaTemplate;
    private final String kafkaTopic;  // Replace with your Kafka topic name

    public KafkaController(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
        this.kafkaTopic = "tweets";  // Replace with your Kafka topic name
    }

    @PostMapping("/kafka/send")
    public String sendMessageToKafka(SingleTweet tweet) {

        System.out.println("\n-----------------------------------\n");
        System.out.println(tweet);
        System.out.println("\n-----------------------------------\n");

        kafkaTemplate.send(kafkaTopic, tweet.toString());
        return "redirect:/home.html";
    }
}
