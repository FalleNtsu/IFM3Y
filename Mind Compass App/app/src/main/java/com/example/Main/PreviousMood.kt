package com.example.Main

data class MoodInfo(val generic_mood:GenericMood, val logged_time: String, val description:String) {
}
data class PreviousMoodResponse(var success:String, val message:String, val payload: ArrayList<PreviousMoods>)
{

}
data class PreviousMoods(val prevMood:MoodInfo){}

data class GenericMood(val name: String)