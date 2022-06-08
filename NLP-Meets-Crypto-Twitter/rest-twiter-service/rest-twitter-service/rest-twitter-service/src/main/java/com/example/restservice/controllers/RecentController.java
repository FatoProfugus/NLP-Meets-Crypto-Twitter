package com.example.restservice.controllers;

import com.example.restservice.services.RecentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class RecentController {
    @Autowired
    RecentService recentService;

    @GetMapping("/recent")
    public ResponseEntity<String> getRecentPost(@RequestParam(value = "keyword", defaultValue = "World") String keyword) {
        return recentService.extractRecent(keyword);
    }

    @GetMapping("/db/recent")
    public ResponseEntity<String> dbRecentSearch(@RequestParam(value = "id", defaultValue = "0") String id) {
        return recentService.findDbRecent(id);
    }

}
