package promotion

const (
	BF_DAY                        = "25"
	BF_MONTH                      = "11"
	BF_TIME_PARSE                 = "01-02"
	BF_PERCENTAGE_DISCOUNT        = 0.10
	BIRTH_DAY_PERCENTAGE_DISCOUNT = 0.05
	USER_TIME_PARSE               = "2006-01-02"
	ISO_LAYOUT                    = "2006-01-02"
)


type (
	// Describe a Promotionary
	Promotionary func(Order) Discount

	// Promotions represente all promotions avalibe to be apply in orders
	Promotions struct {
		Promotion []Promotionary
	}

	// DateISO is the date in ISO 8601
	DateISO string

	// User struct, than represent the date about User in order.
	User struct {
		Date DateISO
	}

	// Order struct, than represent the order cart. If in future the
	// promotions need ve calculate using products in order as a
	// reference, add here the new structs
	Order struct {
		User User
	}

	// Discount struct, than represent a Discount avalibe to be
	Discount struct {
		Percentage  float32
		Description string
	}
)
