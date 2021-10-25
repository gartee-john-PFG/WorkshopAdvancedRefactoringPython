# from approvaltests.approvals import verify
from approvaltests.combination_approvals import verify_all_combinations
from customer import Customer, Movie, Rental

def test_what_does_customer_statement_do():
    customer_name = ["Test Customer"]
    movie_name = ["Star Wars"]
    price_code = [Movie.REGULAR, Movie.NEW_RELEASE, Movie.CHILDRENS]
    days_rented = [2, 3, 4]

    # result = make_statement(customer_name, movie_name, price_code)
    
    # verify(result)
    verify_all_combinations(make_statement,[customer_name, movie_name, price_code, days_rented])

def make_statement(customer_name, movie_name, price_code, days_rented):
    cust = Customer(customer_name)
    movie = Movie(movie_name, ((price_code + 1) % 3))
    rental = Rental(movie, days_rented)
    cust.add_rental(rental)

    movie2 = Movie(movie_name + ": The Sequal", ((price_code + 2) % 3))
    rental2 = Rental(movie2, days_rented)
    cust.add_rental(rental2)  

    movie3 = Movie(movie_name + ":Part III", ((price_code+ 3) % 3))
    rental3 = Rental(movie3, days_rented)
    cust.add_rental(rental3)

    result = cust.statement()
    return result