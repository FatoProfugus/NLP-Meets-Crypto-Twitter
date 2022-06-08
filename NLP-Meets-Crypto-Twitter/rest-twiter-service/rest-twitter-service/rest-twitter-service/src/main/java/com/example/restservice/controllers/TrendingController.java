package com.example.restservice.controllers;

import com.example.restservice.services.TrendingService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TrendingController {
    @Autowired
    TrendingService trendingService;

    @GetMapping("/trending")
    public ResponseEntity<String> getTrendingPost(@RequestParam(value = "place", defaultValue = "1") String place) {
        return trendingService.extractTrending(place);
    }

    @GetMapping("/db/trending")
    public ResponseEntity<String> dbTrendingSearch(@RequestParam(value = "id", defaultValue = "0") String id) {
        return trendingService.findDbTrending(id);
    }

}