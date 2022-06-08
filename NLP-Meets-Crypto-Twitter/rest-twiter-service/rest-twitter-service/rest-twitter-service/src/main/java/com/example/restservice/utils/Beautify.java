package com.example.restservice.utils;

import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;

public class Beautify {
    public static String beautify(String json) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        Object obj = mapper.readValue(json, Object.class);
        return mapper.writerWithDefaultPrettyPrinter().writeValueAsString(obj);
    }
}
