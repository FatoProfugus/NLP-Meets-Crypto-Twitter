package com.example.restservice.services;

import com.example.restservice.dto.RecentPost;
import com.example.restservice.utils.Beautify;
import com.google.gson.Gson;
import okhttp3.Call;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.UUID;

@Service
public class RecentService {
    @Value("${baseTwitterUrl}")
    private String BASE_URL;

    @Value("${twitterBearerToken}")
    private String bearerToken;

    @Autowired
    DbRecent dbRecent;

    private static Logger LOGGER = LoggerFactory.getLogger(RecentService.class);

    public ResponseEntity<String> extractRecent(String keyword) {
        OkHttpClient client = new OkHttpClient();
        String URL = String.format(BASE_URL, keyword);
        try {
            Request request = new Request.Builder()
                    .url(URL)
                    .addHeader("Authorization", bearerToken)
                    .build();

            Call call = client.newCall(request);
            Response response = call.execute();
            String strResponse = Beautify.beautify(response.body().string());
            LOGGER.info(strResponse);
            response.close();
            RecentPost recentPost = new RecentPost(UUID.randomUUID().toString(), strResponse);
            String recentPostJson = new Gson().toJson(recentPost);
            dbRecent.save(recentPost);
            return new ResponseEntity<>(recentPostJson, HttpStatus.OK);
        } catch (Exception e) {
            LOGGER.error(e.toString());
        }
        return new ResponseEntity<>("500 ERROR", HttpStatus.INTERNAL_SERVER_ERROR);
    }

    public ResponseEntity<String> findDbRecent(String uuid) {
        RecentPost dbRecentPost;
        HttpStatus httpStatus;
        try {
            dbRecentPost = dbRecent.findById(uuid).orElseThrow(IndexOutOfBoundsException::new);
            httpStatus = HttpStatus.OK;
        } catch (Exception e) {
            dbRecentPost = new RecentPost(UUID.randomUUID().toString(), "404 error");
            httpStatus = HttpStatus.NOT_FOUND;
            LOGGER.error(e.toString());
        }
        String recentPostJson = new Gson().toJson(dbRecentPost);
        return new ResponseEntity<>(recentPostJson, httpStatus);
    }

}
