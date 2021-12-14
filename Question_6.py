def num_of_cookies(money, price, wrap, num_wraps = 0, cookies = 0):
    """Recursiveliy calculates the number of cookies that can be consumed"""

    #End fo recursion, when there is no more money to buy cookies and no more wrappers
    if money < price and num_wraps < wrap:
        print(cookies)
    else:
        #checks if we have enough money to buy cookies
        if money >= price:
            cookies += money // price   #converting the money into cookies
            money -= cookies * price    #subtracting the prioce of cookies
            num_wraps += cookies        #num_wraps is the current number of wrappers we have, here we convert the cookies into wrappers
        
        #checks if we have enough wrappers to return them for cookies
        if num_wraps >= wrap:
            cookies2 = num_wraps // wrap    #cookies2 contains the number of cookies we get from wrappers
            cookies += cookies2             #updating the number of consumed cookies
            num_wraps -= cookies2 * wrap    #subtracting the number of wrappers we returned for cookies

            #recursive call with the updated money, number of wrappers we have and cookies consumed
            num_of_cookies(money, price, wrap, num_wraps + cookies2, cookies)


def main():
    num_of_cookies(16, 2, 2)

if __name__ == "__main__":
    main()