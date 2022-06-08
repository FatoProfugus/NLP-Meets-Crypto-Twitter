package com.example.restservice.services;

import com.example.restservice.dto.RecentPost;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface DbRecent extends MongoRepository<RecentPost, String> {
}
