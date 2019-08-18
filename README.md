# Games
Games Details Backend Application

1: Plenty type of games stored in db sqlite3
2: Three Backend APIs made:
     * Upload API for uploading games data to db
     * get_all_games API for getting json response of all games details at once
     * get_game_by_title API, which title has to be passed in query parameter so it will search in db any related game with specified title will be extracted.
     * No need to pass complete title just pass remembered string, in API response details will come if any row matched the query string in title field.
3: For all three API user need to pass x-api-key to access, random access is not allowed without API KEY authentication.
4: Django default admin can access all details and can be able to perform crud operations.
5: User is allowed to access get API only.
6: Attched screenshots of postman for reference to API's responses
