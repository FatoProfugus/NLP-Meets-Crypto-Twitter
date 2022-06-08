package com.example.restservice.services;

import com.example.restservice.dto.TrendingPost;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface DbTrending extends MongoRepository<TrendingPost, String> {
}
