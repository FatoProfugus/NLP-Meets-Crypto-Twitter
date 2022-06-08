//package com.example.restservice.controller;
//
//import org.junit.jupiter.api.Test;
//import org.junit.jupiter.api.extension.ExtendWith;
//import org.springframework.beans.factory.annotation.Value;
//import org.springframework.test.context.TestPropertySource;
//import org.springframework.test.context.junit.jupiter.SpringExtension;
//
//@ExtendWith(SpringExtension.class)
//@TestPropertySource(locations = "classpath:application-test.properties")
//public class RecentControllerTest {
//
//    private final String baseUrl = "/v1/fields";
//
//    @Value("${port}")
//    private String port;
//
//    @Value("${path}")
//    private String context_path;
//
//    @Test
//    public void checkProperties() {
//        String localHostUrl = "http://localhost:" + port + context_path + baseUrl;
//        System.out.println(port);
//        System.out.println(context_path);
//        System.out.println(localHostUrl);
//    }
//
//}