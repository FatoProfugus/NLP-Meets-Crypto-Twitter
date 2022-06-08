package com.example.restservice.dto;

import lombok.Data;
import lombok.NonNull;
import org.springframework.data.annotation.Id;

@Data
public class TrendingPost {
    @Id
    @NonNull
    String id;
    @NonNull
    private String content;

    public TrendingPost() {
    }

    public TrendingPost(String id, String content) {
        this.id = id;
        this.content = content;
    }

}