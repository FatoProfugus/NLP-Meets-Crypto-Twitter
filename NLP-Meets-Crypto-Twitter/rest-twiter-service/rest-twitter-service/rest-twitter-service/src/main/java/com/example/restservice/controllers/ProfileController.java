package com.example.restservice.controllers;

import com.example.restservice.services.ProfileService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
public class ProfileController {
    @Autowired
    ProfileService profileService;

    @GetMapping("/profile")
    public String getProfileTweets(@RequestParam List<String> key) {
        return profileService.extractTweets(key.get(0), key.get(1), key.get(2));
    }

}
