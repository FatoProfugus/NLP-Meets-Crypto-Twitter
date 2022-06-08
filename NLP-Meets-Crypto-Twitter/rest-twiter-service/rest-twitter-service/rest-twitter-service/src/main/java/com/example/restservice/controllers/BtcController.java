package com.example.restservice.controllers;

import com.example.restservice.services.BtcService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class BtcController {
    @Autowired
    BtcService btcService;

    @GetMapping("/btc")
    public String getProfileTweets(@RequestParam List<String> key) {
        return btcService.extractTweets(key.get(0), key.get(1));
    }

}
