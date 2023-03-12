package com.pivden.sawebapp;

import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@CrossOrigin(origins = "*")
@RestController
public class SentimentController {

    @PostMapping("/sentiment")
    public SentimentDto sentimentAnalysis(@RequestBody SentenceDto sentenceDto) {
        RestTemplate restTemplate = new RestTemplate();
        System.out.println(sentenceDto);
        return restTemplate.postForEntity("http://logic:5000/analyse/sentiment",
                        sentenceDto, SentimentDto.class)
                .getBody();
    }

    @GetMapping("/testHealth")
    public String testHealth() {
        return "Health";
    }
}


