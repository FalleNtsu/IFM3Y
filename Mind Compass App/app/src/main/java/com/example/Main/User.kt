package com.example.Main

import java.util.*

data class User (val id: Int,
                 val username: String,
                 val email_address: String,
                 val password: String,
                 val tile: String,
                 val first_name: String,
                 val surname: String,
                 val cell_number: String,
                 val date_of_birth: Date,
                 val gender: String,
                 val primary_address: String,
                 val city: String,
                 val postal_code: String,
                 val country: String,
                 val citizenship: String,
                 val is_inactive: Boolean,
                 val created_at: Date,
                 val updated_at: Date){

}