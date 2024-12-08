class Session():
    """Stores user_id, username and logged in status"""
    def __init__(self, user_id: int = None, username: str = None, logged_in: bool = False) -> None:
        self.user_id = user_id
        self.username = username
        self.logged_in = logged_in
        
    def get_username(self) -> str:
        return self.username
    
    def get_login_status(self) -> bool:
        return self.logged_in
    
    def get_user_id(self) -> int:
        return self.user_id
    
    def set_user_login(self, user_id: int, username:str) -> None:
        self.user_id = user_id
        self.username = username
        self.logged_in = True
    
    def clear_session(self) -> None:
        self.user_id = None
        self.username = None
        self.logged_in = False