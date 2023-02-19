from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import sqlite3


ui, _ = loadUiType("./zakat_donation_platform.ui")


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.current_user = "admin"
        self.tabWidget.setCurrentIndex(0)
        self.LoginButton.clicked.connect(self.login)
        self.adm_logout.clicked.connect(self.logout)
        self.don_logout.clicked.connect(self.logout)
        self.rep_logout.clicked.connect(self.logout)
        self.signin_button.clicked.connect(self.register)
        self.don_update.clicked.connect(self.don_updt)
        self.rep_update.clicked.connect(self.rep_updt)
        self.adm_upd.clicked.connect(self.adm_updt)
        self.don_conf.clicked.connect(self.donation)
        self.show_don_data.clicked.connect(self.dondata)
        self.show_rep_data.clicked.connect(self.rcvdata)
        self.show_adm_data.clicked.connect(self.admdat)
        self.admcombo()
        self.show_av_rep.activated[str].connect(self.onChanged)
        self.adm_conf.clicked.connect(self.trnx)

    def ckdb(self, un, pas):
        connection = sqlite3.connect("zakat_donation_db.db")
        cur = connection.cursor()
        cur.execute(
            """SELECT user_name,password
            FROM login
            WHERE user_name = ? AND password = ?""", (un, pas))
        if (cur.fetchone()):
            connection.commit()
            connection.close()
            return True
        else:
            connection.commit()
            connection.close()
            return False

# user login logout

    def login(self):
        connection = sqlite3.connect("zakat_donation_db.db")
        cur = connection.cursor()
        username = self.user_name.text()
        password = self.password.text()
        if (self.ckdb(username, password)):
            self.user_name.setText("")
            self.password.setText("")
            cur.execute(
                "SELECT type FROM login WHERE user_name = ?", (username,))
            type = cur.fetchall()
            if (type[0][0] == 'a'):
                self.tabWidget.setCurrentIndex(3)
            elif (type[0][0] == 'd'):
                self.tabWidget.setCurrentIndex(1)
            else:
                self.tabWidget.setCurrentIndex(2)

            self.current_user = username
        else:
            self.login_error.setText("Invalid details")
        connection.commit()
        connection.close()

    def logout(self):
        self.tabWidget.setCurrentIndex(0)
        self.current_user = ""

# user registration

    def register(self):
        un = self.signin_username.text()
        pas = self.signin_password.text()

        if (self.signin_as_don.isChecked()):
            val = 'd'
        elif (self.signin_as_rep.isChecked()):
            val = 'r'
        else:
            val = 'a'

        connection = sqlite3.connect("zakat_donation_db.db")
        curs = connection.cursor()
        curs.execute("SELECT * FROM login WHERE user_name = ? ", (un,))
        if (curs.fetchone()):
            self.signin_error.setText("Invalid username")
        else:
            curs.execute(
                """INSERT INTO login(user_name,password,type) VALUES(?,?,?)""", (un, pas, val))
            self.signin_error.setText("signin success")

            self.signin_username.setText("")
            self.signin_password.setText("")

        connection.commit()
        connection.close()

# donor rep admin data update

    def don_updt(self):
        ssn = self.don_nid.text()
        fname = self.don_fname.text()
        lname = self.don_lname.text()
        add = self.don_add.text()
        mail = self.don_mail.text()
        rel = self.don_rel.text()
        connection = sqlite3.connect("zakat_donation_db.db")
        curs = connection.cursor()
        curs.execute("SELECT * FROM donor WHERE user_name = ? ",
                     (self.current_user,))
        if (curs.fetchone()):
            curs.execute("""UPDATE donor SET ssn = ?,first_name = ?,last_name=?,address=?,email=?,relegion=? WHERE user_name = ?""",
                         (ssn, fname, lname, add, mail, rel,  self.current_user,))
        else:
            curs.execute("""INSERT INTO donor VALUES(?,?,?,?,?,?,?)""",
                         (ssn, fname, lname, add, mail, rel, self.current_user))
        connection.commit()
        connection.close()

    def rep_updt(self):
        cmpid = self.rep_cmp_id.text()
        cmpn = self.rep_cmp_name.text()
        add = self.rep_add.text()
        mail = self.rep_mail.text()
        city = self.rep_city.text()
        connection = sqlite3.connect("zakat_donation_db.db")
        curs = connection.cursor()
        curs.execute("SELECT * FROM representative WHERE user_name = ? ",
                     (self.current_user,))
        if (curs.fetchone()):
            curs.execute("""UPDATE representative SET company_id = ?,company_name = ?,address=?,email=?,city=? WHERE user_name = ?""",
                         (cmpid, cmpn, add, mail, city,  self.current_user,))
        else:
            curs.execute("""INSERT INTO representative VALUES(?,?,?,?,?,?)""",
                         (cmpid, cmpn, add, city, mail, self.current_user))
        connection.commit()
        connection.close()

    def adm_updt(self):
        name = self.adm_name.text()
        email = self.adm_mail.text()
        connection = sqlite3.connect("zakat_donation_db.db")
        curs = connection.cursor()
        curs.execute("SELECT * FROM admin WHERE user_name = ? ",
                     (self.current_user,))
        if (curs.fetchone()):
            curs.execute("""UPDATE admin SET name = ?,email = ? WHERE user_name = ?""",
                         (name,  email, self.current_user,))
        else:
            curs.execute("""INSERT INTO admin(name,email,user_name) VALUES(?,?,?)""",
                         (name, email, self.current_user))
        connection.commit()
        connection.close()

# donr gives donation

    def donation(self):
        charity = self.don_giv_char.text()
        zak = self.don_giv_zak.text()
        tnx = self.don_tnx.text()
        connection = sqlite3.connect("zakat_donation_db.db")
        cursor = connection.cursor()
        cursor.execute("SELECT ssn FROM donor WHERE user_name =?",
                       (self.current_user,))
        id = cursor.fetchone()[0][0]
        cursor.execute(
            "INSERT INTO donation(don_id,given_charity,given_zakat,tnx_number) VALUES(?,?,?,?)", (id, charity, zak, tnx))
        cursor.execute(
            "SELECT tot_zak, tot_char FROM donor WHERE ssn = ?", (id,))
        data = cursor.fetchall()
        zak += data[0][0]
        charity += data[0][1]
        cursor.execute(
            "UPDATE donor SET tot_zak = ?, tot_char=? WHERE ssn=?", (zak, charity, id))
        connection.commit()
        connection.close()

# don data show

    def dondata(self):
        connection = sqlite3.connect("zakat_donation_db.db")
        cursor = connection.cursor()
        cursor.execute("SELECT tot_zak,tot_char FROM donor WHERE user_name =?",
                       (self.current_user,))
        data = cursor.fetchall()
        self.don_ed_charity.setText(str(data[0][1]))
        self.don_ed_zakat.setText(str(data[0][0]))
        connection.commit()
        connection.close()

# rcv data show
    def rcvdata(self):
        connection = sqlite3.connect("zakat_donation_db.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT recv_charity,recv_zakat
                FROM representative
                JOIN received_amount ON representative.company_id = received_amount.rep_id
                WHERE user_name =?""",
                       (self.current_user,))

        data = cursor.fetchall()
        tot_zak = tot_char = 0
        for i in data:
            tot_zak += i[1]
            tot_char += i[0]
        self.rep_show_av_char.setText(str(tot_char))
        self.rep_show_av_zak.setText(str(tot_zak))
        connection.commit()
        connection.close()

# admin show data

    def admdat(self):
        connection = sqlite3.connect("zakat_donation_db.db")
        cursor = connection.cursor()
        cursor.execute(
            "SELECT sum(given_charity) as charity,sum(given_zakat) as zakat FROM donation ")
        data = cursor.fetchall()
        self.adm_av_zak.setText(str(data[0][1]))
        self.adm_av_char.setText(str(data[0][0]))
        connection.commit()
        connection.close()

# admin rep combo box
    def admcombo(self):
        connection = sqlite3.connect("zakat_donation_db.db")
        cursor = connection.cursor()
        cursor.execute(
            """SELECT company_name FROM representative """)
        data = cursor.fetchall()
        for i in data:
            self.show_av_rep.addItem(i[0])
# combo box data show

    def onChanged(self, usr):
        connection = sqlite3.connect("zakat_donation_db.db")
        cursor = connection.cursor()
        cursor.execute("""SELECT recv_charity,recv_zakat
                FROM representative
                JOIN received_amount ON representative.company_id = received_amount.rep_id
                WHERE company_name =?""",
                       (usr,))

        data = cursor.fetchall()
        tot_zak = tot_char = 0
        for i in data:
            tot_zak += i[1]
            tot_char += i[0]
        self.adm_sho_rcv_chr.setText(str(tot_char))
        self.adm_sho_rcv_zak.setText(str(tot_zak))
        connection.commit()
        connection.close()

# transaction

    def trnx(self):
        zak = self.adm_giv_zak.text()
        chr = self.adm_giv_chr.text()
        connection = sqlite3.connect("zakat_donation_db.db")
        cursor = connection.cursor()
        cursor.execute("SELECT company_id FROM representative WHERE company_name='" +
                       self.show_av_rep.currentText()+"'")
        data = cursor.fetchall()
        rep = data[0][0]
        cursor.execute(
            "INSERT INTO received_amount(rep_id,recv_charity,recv_zakat) VALUES(?,?,?)", (rep, chr, zak))
        connection.commit()
        cursor.execute(
            "SELECT tranx_id FROM received_amount ORDER BY tranx_id DESC LIMIT 1")
        data = cursor.fetchall()
        reptid = (data[0][0])
        cursor.execute(
            "SELECT admin_id FROM admin WHERE user_name=?", (self.current_user,))
        data = cursor.fetchall()
        admid = (data[0][0])
        cursor.execute(
            "INSERT INTO transx(adm_id,recv_tid) VALUES(?,?)", (admid, reptid,))
        connection.commit()
        z = int(zak)
        c = int(chr)
        while z > 0:
            cursor.execute(
                "SELECT tranx_id,given_zakat FROM donation WHERE given_zakat > 0 ORDER BY given_zakat asc LIMIT 1")
            data = cursor.fetchall()
            trnxID = data[0][0]
            zakat = data[0][1]
            if z >= zakat:
                cursor.execute(
                    "UPDATE donation SET given_zakat = ? WHERE tranx_id = ?", (0, trnxID))
                p = zakat
                z = z - zakat
            else:
                cursor.execute(
                    "UPDATE donation SET given_zakat = ? WHERE tranx_id = ?", (zakat-z, trnxID))
                p = zakat-z
                z = 0
            cursor.execute(
                "SELECT * FROM donor_list WHERE don_tid = ? AND rcv_tid = ?", (trnxID, reptid))

            if (cursor.fetchone()):
                cursor.execute(
                    "UPDATE donor_list SET zakat = ? WHERE rcv_tid=?AND don_tid=?", (p, reptid, trnxID))
            else:
                cursor.execute(
                    "INSERT INTO donor_list(don_tid,rcv_tid,zakat)VALUES(?,?,?)", (trnxID, reptid, p))
            connection.commit()

        while c > 0:
            cursor.execute(
                "SELECT tranx_id,given_charity FROM donation WHERE given_charity > 0 ORDER BY given_charity asc LIMIT 1")
            data = cursor.fetchall()
            trnxID = data[0][0]
            charity = data[0][1]
            if c >= charity:
                cursor.execute(
                    "UPDATE donation SET given_charity = ? WHERE tranx_id = ?", (0, trnxID))
                p = charity
                c = c - charity
            else:
                cursor.execute(
                    "UPDATE donation SET given_charity = ? WHERE tranx_id = ?", (charity-c, trnxID))
                p = charity-c
                c = 0
            cursor.execute(
                "SELECT * FROM donor_list WHERE don_tid = ? AND rcv_tid = ?", (trnxID, reptid))

            if (cursor.fetchone()):
                cursor.execute(
                    "UPDATE donor_list SET charity = ? WHERE rcv_tid=?AND don_tid=?", (p, reptid, trnxID))
            else:
                cursor.execute(
                    "INSERT INTO donor_list(don_tid,rcv_tid,charity) VALUES(?,?,?)", (trnxID, reptid, c))
            connection.commit()
        connection.close()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
