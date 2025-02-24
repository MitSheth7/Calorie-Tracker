package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// Food represents a food entry with nutritional information.
type Food struct {
	Name     string `json:"name"`
	Calories int    `json:"calories"`
	Protein  int    `json:"protein"`
	Fat      int    `json:"fat"`
	Carbs    int    `json:"carbs"`
}

// foodEntries will store all food items received.
var foodEntries []Food

func main() {
	// Initialize the Gin router.
	router := gin.Default()

	// Endpoint to add a new food entry.
	router.POST("/food", func(c *gin.Context) {
		var newFood Food
		// Bind the JSON payload to our Food struct.
		if err := c.ShouldBindJSON(&newFood); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}
		foodEntries = append(foodEntries, newFood)
		c.JSON(http.StatusOK, gin.H{"status": "Food added", "food": newFood})
	})

	// Endpoint to get the nutritional summary.
	router.GET("/summary", func(c *gin.Context) {
		totalCalories, totalProtein, totalFat, totalCarbs := 0, 0, 0, 0
		// Sum up the nutritional values.
		for _, food := range foodEntries {
			totalCalories += food.Calories
			totalProtein += food.Protein
			totalFat += food.Fat
			totalCarbs += food.Carbs
		}
		// Create and return a summary.
		summary := gin.H{
			"calories": totalCalories,
			"protein":  totalProtein,
			"fat":      totalFat,
			"carbs":    totalCarbs,
		}
		c.JSON(http.StatusOK, summary)
	})

	// Start the server on port 8080.
	router.Run(":8080")
}
