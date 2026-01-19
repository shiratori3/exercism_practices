package booking

import (
	"fmt"
	"time"
)

const (
	layout1 = "1/2/2006 15:04:05"
	layout2 = "January 2, 2006 15:04:05"
	layout3 = "Monday, January 2, 2006 15:04:05"
)

// Schedule returns a time.Time from a string containing a date.
func Schedule(date string) time.Time {
	t, err := time.Parse(layout1, date)
	if err != nil {
		panic(err)
	}
	return t
}

// HasPassed returns whether a date has passed.
func HasPassed(date string) bool {
	now := time.Now()
	t, err := time.Parse(layout2, date)
	if err != nil {
		panic(err)
	}
	if now.After(t) {
		return true
	} else {
		return false
	}
}

// IsAfternoonAppointment returns whether a time is in the afternoon.
func IsAfternoonAppointment(date string) bool {
	t, err := time.Parse(layout3, date)
	if err != nil {
		panic(err)
	}
	h := t.Hour()
	if h >= 12 && h < 18 {
		return true
	}
	return false
}

// Description returns a formatted string of the appointment time.
func Description(date string) string {
	t := Schedule(date)
	return fmt.Sprintf("You have an appointment on %s, %s %d, %d, at %d:%d.",
		t.Weekday(), t.Month(), t.Day(), t.Year(), t.Hour(), t.Minute())
}

// AnniversaryDate returns a Time with this year's anniversary.
func AnniversaryDate() time.Time {
	year := time.Now().Year()
	return time.Date(year, time.September, 15, 0, 0, 0, 0, time.UTC)
}
