import sqlite3

class Database:

    def __init__(self):

        self.conn = sqlite3.connect('muxdb.sqlite', check_same_thread = False)

    def setup(self):

        cmd = """CREATE TABLE IF NOT EXISTS muxbot(
        user_id INT,
        vid_name TEXT,
        sub_name TEXT,
        filename TEXT
        );"""

        self.conn.execute(cmd)
        self.conn.commit()

    def put_video(self, user_id, vid_name, filename):

        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        up_cmd = f'UPDATE muxbot SET vid_name="{vid_name}", filename="{filename}" WHERE user_id={user_id};'
        data = (user_id, vid_name, None, filename)
        if res := self.conn.execute(srch_cmd).fetchone():
            self.conn.execute(up_cmd)
        else:
            ins_cmd = 'INSERT INTO muxbot VALUES (?,?,?,?);'
            self.conn.execute(ins_cmd,data)
        self.conn.commit()

    def put_sub(self,user_id,sub_name):

        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        up_cmd = f'UPDATE muxbot SET sub_name="{sub_name}" WHERE user_id={user_id};'
        data = (user_id,None,sub_name,None)

        if res := self.conn.execute(srch_cmd).fetchone():
            self.conn.execute(up_cmd)
        else:
            ins_cmd = 'INSERT INTO muxbot VALUES (?,?,?,?);'
            self.conn.execute(ins_cmd,data)
        self.conn.commit()

    def check_sub(self,user_id):

        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'

        if res := self.conn.execute(srch_cmd).fetchone():
            return bool(sub_file := res[2])
        else:
            return False

    def check_video(self,user_id):

        srch_cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        if res := self.conn.execute(srch_cmd).fetchone():
            return bool(vid_file := res[1])
        else:
            return False

    def get_vid_filename(self, user_id):

        cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        return res[1] if (res := self.conn.execute(cmd).fetchone()) else False

    def get_sub_filename(self, user_id):

        cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        return res[2] if (res := self.conn.execute(cmd).fetchone()) else False

    def get_filename(self, user_id):

        cmd = f'SELECT * FROM muxbot WHERE user_id={user_id};'
        return res[3] if (res := self.conn.execute(cmd).fetchone()) else False

    def erase(self,user_id) :

        erase_cmd = f'DELETE FROM muxbot WHERE user_id={user_id} ;'

        try :
            self.conn.execute(erase_cmd)
            self.conn.commit()
            return True
        except :
            return False
