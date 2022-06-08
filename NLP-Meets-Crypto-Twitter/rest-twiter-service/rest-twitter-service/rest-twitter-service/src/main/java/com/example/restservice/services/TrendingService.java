package com.example.restservice.services;

import com.example.restservice.dto.TrendingPost;
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
public class TrendingService {
    @Value("${baseTwitterUrl}")
    private String BASE_URL;

    @Value("${twitterBearerToken}")
    private String bearerToken;

    @Autowired
    DbTrending dbTrending;

    private static Logger LOGGER = LoggerFactory.getLogger(TrendingService.class);

    public ResponseEntity<String> extractTrending(String keyword) {
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
            TrendingPost trendingPost = new TrendingPost(UUID.randomUUID().toString(), strResponse);
            String trendingPostJson = new Gson().toJson(trendingPost);
            dbTrending.save(trendingPost);
            return new ResponseEntity<>(trendingPostJson, HttpStatus.OK);
        } catch (Exception e) {
            LOGGER.error(e.toString());
        }
        return new ResponseEntity<>("500 ERROR", HttpStatus.INTERNAL_SERVER_ERROR);
    }

    public ResponseEntity<String> findDbTrending(String uuid) {
        TrendingPost dbTrendingPost;
        HttpStatus httpStatus;
        try {
            dbTrendingPost = dbTrending.findById(uuid).orElseThrow(IndexOutOfBoundsException::new);
            httpStatus = HttpStatus.OK;
        } catch (Exception e) {
            dbTrendingPost = new TrendingPost(UUID.randomUUID().toString(), "404 error");
            httpStatus = HttpStatus.NOT_FOUND;
            LOGGER.error(e.toString());
        }
        String trendingPostJson = new Gson().toJson(dbTrendingPost);
        return new ResponseEntity<>(trendingPostJson, httpStatus);
    }

}
