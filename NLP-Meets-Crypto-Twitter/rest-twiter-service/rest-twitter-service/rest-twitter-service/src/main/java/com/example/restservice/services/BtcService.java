package com.example.restservice.services;

import com.example.restservice.utils.Beautify;
import okhttp3.*;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class BtcService {
    @Value("${btcTwitterUrl}")
    private String BASE_URL;

    @Value("${twitterBearerToken}")
    private String bearerToken;

    public String extractTweets(String startingDate, String endingDate) {
        OkHttpClient client = new OkHttpClient();
        String URL = String.format(BASE_URL, startingDate, endingDate);
        String strResponse;
        try {
            Request request = new Request.Builder()
                    .url(URL)
                    .addHeader("Authorization", bearerToken)
                    .build();

            Call call = client.newCall(request);
            Response response = call.execute();
            strResponse = response.body().string();
            response.close();
            return Beautify.beautify(strResponse);
        } catch (Exception e) {
            System.out.println(e.toString());
        }
        return null;
    }

}
