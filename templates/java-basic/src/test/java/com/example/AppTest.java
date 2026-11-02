package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppTest {

    @Test
    void shouldReturnCorrectMessage() {
        String result = App.getMessage();

        assertEquals("Projeto Java funcionando!", result);
    }
}
