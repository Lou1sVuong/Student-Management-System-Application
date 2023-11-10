from PyQt5 import QtGui, QtWidgets, QtCore
from loginUi import Ui_Form
from MainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import sys
import os
class LoginApp(QtWidgets.QWidget, Ui_Form):
    
    #hàm nút switch form
    def changeForm(self):
        if self.switch_btn.isChecked():
            self.widget_2.hide()
            self.widget_3.show()
            self.switch_btn.setText("《")
        else:
            self.widget_2.show()
            self.widget_3.hide()
            self.switch_btn.setText("》")
            
    #hàm nút đóng mở        
    def minimizeApp(self):
        self.showMinimized()

    def closeApp(self):
        self.close()
           
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #login_btn
        self.login_btn.clicked.connect(self.loginCheck)
        #reg_btn
        self.reg_btn.clicked.connect(self.registerUser)

        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.login_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.reg_btn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.widget_3.hide()
        #nút switch
        self.switch_btn.clicked.connect(self.changeForm)
        #nút đóng mở
        self.exit_btn.clicked.connect(self.closeApp)
        self.minimized_btn.clicked.connect(self.minimizeApp)
    #dangNhap
    def loginCheck(self):
        username = self.userName.text()
        password = self.password.text()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/login.db')
        try:
            # Kết nối đến CSDL SQLite với đường dẫn tuyệt đối
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        
            user = cursor.fetchone()
            conn.close()

            if user is not None:
                self.show_main_window()
            else:
                QtWidgets.QMessageBox.warning(self, "Đăng nhập không thành công", "Tên người dùng hoặc mật khẩu không đúng.")
        except sqlite3.Error as e:
            print("Lỗi SQLite:", e)
    #dangKy
    def registerUser(self):
        username = self.userName_reg.text()
        password = self.password_reg.text()
        confirm_password = self.cf_password.text()

        # Kiểm tra xem tên người dùng và mật khẩu có bị bỏ trống không
        if not username or not password or not confirm_password:
            QtWidgets.QMessageBox.warning(self, "Đăng ký không thành công", "Tên người dùng và mật khẩu không được để trống.")
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/login.db')

        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
            existing_user = cursor.fetchone()

            if existing_user is not None:
                QtWidgets.QMessageBox.warning(self, "Đăng ký không thành công", "Tên người dùng đã tồn tại.")
            elif password == confirm_password:
                cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
                conn.commit()
                conn.close()

                self.widget_3.hide()
                self.widget_2.show()
                self.switch_btn.setText("》")
            else:
                QtWidgets.QMessageBox.warning(self, "Đăng ký không thành công", "Mật khẩu và xác nhận mật khẩu không trùng nhau.")
        except sqlite3.Error as e:
            print("Lỗi SQLite:", e)
    #di chuyển cửa sổ
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
   
    def show_main_window(self):
        self.hide()
        self.main_window = MainWindow()
        self.main_window.show()
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    # #di chuyển cửa sổ
    # def mousePressEvent(self, event):
    #     if event.button() == QtCore.Qt.LeftButton:
    #         self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
    #         event.accept()
    # def mouseMoveEvent(self, event):
    #     if event.buttons() == QtCore.Qt.LeftButton:
    #         self.move(event.globalPos() - self.dragPosition)
    #         event.accept()
   
    #đóng mở đăng xuất...
    def minimizeApp(self):
        self.showMinimized()

    def closeApp(self):
        confirm = QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn thoát ứng dụng?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close()
        
    def maximizeApp(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def restoreApp(self):
        self.showNormal()

    def logout(self):
        confirm = QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn đăng xuất?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            self.close() 
            self.login_window = LoginApp()  
            self.login_window.show() 
    ########
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        #làm tí shadow ha
        self.pushButton_Student.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton_Class.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.pushButton_Subject.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.pushButton_Grades.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.groupBox_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.groupBox_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.groupBox_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.groupBox_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        #chuyển tab
        self.stackedWidget.setCurrentWidget(self.page_Stu)
        self.pushButton_Student.clicked.connect(lambda: self.changePage(1))
        self.pushButton_Class.clicked.connect(lambda: self.changePage(2))
        self.pushButton_Subject.clicked.connect(lambda: self.changePage(3))
        self.pushButton_Grades.clicked.connect(lambda: self.changePage(4))
        #nút đóng mở
        self.maximize_btn.clicked.connect(self.maximizeApp)
        self.close_btn.clicked.connect(self.closeApp)
        self.minimize_sign_btn.clicked.connect(self.minimizeApp)
        
        #menu
        self.frame_control.setVisible(True)
        self.menu_btn.clicked.connect(self.menuCheck)
        
        #load data lên table
        self.load_student_data()

        # Kết nối sự kiện double-click cho các bảng
        self.tableWidget_STD.cellDoubleClicked.connect(self.populateTextEditsForStudent)
        self.tableWidget_STD_2.cellDoubleClicked.connect(self.populateTextEditsForClass)
        self.tableWidget_STD_3.cellDoubleClicked.connect(self.populateTextEditsForSubject)
        self.tableWidget_STD_6.cellDoubleClicked.connect(self.populateTextEditsForGrades)

        self.logout_btn.clicked.connect(self.logout)
        
        # Kết nối các nút với các chức năng tương ứng trên trang "page_Stu"
        self.insert_btn_STD.clicked.connect(self.insertStudent)
        self.update_btn_STD.clicked.connect(self.updateStudent)
        self.delete_btn_STD.clicked.connect(self.deleteStudent)
        self.clear_btn_STD.clicked.connect(self.clearStudent)
        self.search_btn_STD.clicked.connect(self.searchStudent)
        # Kết nối các nút với các chức năng tương ứng trên trang "page_Classes"
        self.insert_btn_Class.clicked.connect(self.insertClasses)
        self.update_btn_Class.clicked.connect(self.updateClasses)
        self.delete_btn_Class.clicked.connect(self.deleteClasses)
        self.clear_btn_Class.clicked.connect(self.clearClasses)
        self.search_btn_Class.clicked.connect(self.searchClasses)
        # Kết nối các nút với các chức năng tương ứng trên trang "page_Subject"
        self.insert_btn_Sub.clicked.connect(self.insertSubject)
        self.update_btn_Sub.clicked.connect(self.updateSubject)
        self.delete_btn_Sub.clicked.connect(self.deleteSubject)
        self.clear_btn_Sub.clicked.connect(self.clearSubject)
        self.search_btn_Sub.clicked.connect(self.searchSubject)
        # Kết nối các nút với các chức năng tương ứng trên trang "page_Grades"
        self.insert_btn_Grades.clicked.connect(self.insertGrades)
        self.update_btn_Grades.clicked.connect(self.updateGrades)
        self.delete_btn_Grades.clicked.connect(self.deleteGrades)
        self.clear_btn_Grades.clicked.connect(self.clearGrades)
        self.search_btn_Grades.clicked.connect(self.searchGrades)

        #sort_btn
        self.sort_btn_Stu.clicked.connect(self.sortTableStu)
        self.default_btn_Stu.clicked.connect(self.resetTableStu)
        
        self.sort_btn_Class.clicked.connect(self.sortTableClass)
        self.default_btn_Class.clicked.connect(self.resetTableClass)
        
        self.sort_btn_Sub.clicked.connect(self.sortTableSub)
        self.default_btn_Sub.clicked.connect(self.resetTableSub)
        
        self.sort_btn_Grades.clicked.connect(self.sortTableGrades)
        self.default_btn_Grades.clicked.connect(self.resetTableGrades)
        
    def menuCheck(self):
        if self.frame_control.isVisible():
            self.frame_control.setVisible(False)
        else:
            self.frame_control.setVisible(True)
  
    def changePage( self , index ):
        if index == 1:
            self.stackedWidget.setCurrentWidget(self.page_Stu)
        elif index == 2:
            self.stackedWidget.setCurrentWidget(self.page_Class)
        elif index == 3:
            self.stackedWidget.setCurrentWidget(self.page_Subject)
        else:
            self.stackedWidget.setCurrentWidget(self.page_StuGrades)

    def load_student_data(self):
        # Đường dẫn đến thư mục chứa file cơ sở dữ liệu "smdb.db"
        database_dir = os.path.join(os.path.dirname(__file__), 'dataBase')
        database_path = os.path.join(database_dir, 'smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Thực hiện truy vấn SQL để lấy dữ liệu từ bảng "Student"
        cursor.execute("SELECT * FROM Student")
        data = cursor.fetchall()
        # Điền dữ liệu vào QTableWidget
        self.tableWidget_STD.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data))
                self.tableWidget_STD.setItem(row_idx, col_idx, item)
                
                
                
        # Thực hiện truy vấn SQL để lấy dữ liệu từ bảng "Class"
        cursor.execute("SELECT * FROM Classes")
        data = cursor.fetchall()
        # Điền dữ liệu vào QTableWidget
        self.tableWidget_STD_2.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data))
                self.tableWidget_STD_2.setItem(row_idx, col_idx, item)
 
 
         # Thực hiện truy vấn SQL để lấy dữ liệu từ bảng "Subject"
        cursor.execute("SELECT * FROM Subject")
        data = cursor.fetchall()
        # Điền dữ liệu vào QTableWidget
        self.tableWidget_STD_3.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data))
                self.tableWidget_STD_3.setItem(row_idx, col_idx, item)
                
         # Thực hiện truy vấn SQL để lấy dữ liệu từ bảng "Grades"
        cursor.execute("SELECT * FROM StudentGrades")
        data = cursor.fetchall()
        # Điền dữ liệu vào QTableWidget
        self.tableWidget_STD_6.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data))
                self.tableWidget_STD_6.setItem(row_idx, col_idx, item)
        # Đóng kết nối đến cơ sở dữ liệu SQLite
        conn.close()
        
        self.tableWidget_STD.itemSelectionChanged.connect(self.selectRowFromCell)
        self.tableWidget_STD_2.itemSelectionChanged.connect(self.selectRowFromCell)
        self.tableWidget_STD_3.itemSelectionChanged.connect(self.selectRowFromCell)
        self.tableWidget_STD_6.itemSelectionChanged.connect(self.selectRowFromCell)
        
        # Áp dụng màu xám kẻ cho các hàng
        for row_idx in range(self.tableWidget_STD.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD.columnCount()):
                    item = self.tableWidget_STD.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
                    
        for row_idx in range(self.tableWidget_STD_2.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_2.columnCount()):
                    item = self.tableWidget_STD_2.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
                    
        for row_idx in range(self.tableWidget_STD_3.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_3.columnCount()):
                    item = self.tableWidget_STD_3.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
                    
        for row_idx in range(self.tableWidget_STD_6.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_6.columnCount()):
                    item = self.tableWidget_STD_6.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
  

        
        # Tính toán kích thước cột cho mỗi bảng
        def evenly_distribute_columns(table_widget):
            total_columns = table_widget.columnCount()
            if total_columns > 0:
                column_width = table_widget.width() // total_columns
                for col_idx in range(total_columns):
                    table_widget.setColumnWidth(col_idx, column_width)

        # Gọi hàm evenly_distribute_columns cho từng bảng
        evenly_distribute_columns(self.tableWidget_STD)
        evenly_distribute_columns(self.tableWidget_STD_2)
        evenly_distribute_columns(self.tableWidget_STD_3)
        evenly_distribute_columns(self.tableWidget_STD_6)
        
        def set_table_read_only(table_widget):
            for row in range(table_widget.rowCount()):
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        
        set_table_read_only(self.tableWidget_STD)
        set_table_read_only(self.tableWidget_STD_2)
        set_table_read_only(self.tableWidget_STD_3)
        set_table_read_only(self.tableWidget_STD_6)
        
    def selectRowFromCell(self):
        selected_items = self.tableWidget_STD.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            for col_idx in range(self.tableWidget_STD.columnCount()):
                item = self.tableWidget_STD.item(selected_row, col_idx)
                item.setSelected(True)
        
        selected_items = self.tableWidget_STD_2.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            for col_idx in range(self.tableWidget_STD_2.columnCount()):
                item = self.tableWidget_STD_2.item(selected_row, col_idx)
                item.setSelected(True)
        
        selected_items = self.tableWidget_STD_3.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            for col_idx in range(self.tableWidget_STD_3.columnCount()):
                item = self.tableWidget_STD_3.item(selected_row, col_idx)
                item.setSelected(True)
                
        selected_items = self.tableWidget_STD_6.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            for col_idx in range(self.tableWidget_STD_6.columnCount()):
                item = self.tableWidget_STD_6.item(selected_row, col_idx)
                item.setSelected(True)

    def populateTextEditsForStudent(self, row, col):
            selected_row_data = []
            for col_idx in range(self.tableWidget_STD.columnCount()):
                item = self.tableWidget_STD.item(row, col_idx)
                if item is not None:
                    selected_row_data.append(item.text())

            # Điền dữ liệu vào các textEdit tương ứng
            if len(selected_row_data) >= 4:
                self.getStudentID_STD.setText(selected_row_data[0])
                self.getStudentName_STD.setText(selected_row_data[1])
                self.getStudentAddress_STD.setText(selected_row_data[2])
                self.getClassID_STD.setText(selected_row_data[3])
                
    def populateTextEditsForClass(self, row, col):
        selected_row_data = []
        for col_idx in range(self.tableWidget_STD_2.columnCount()):
            item = self.tableWidget_STD_2.item(row, col_idx)
            if item is not None:
                selected_row_data.append(item.text())

        # Điền dữ liệu vào các textEdit tương ứng
        if len(selected_row_data) >= 3:
            self.getClassID_Class.setText(selected_row_data[0])
            self.getClassName_Class.setText(selected_row_data[1])
            self.getClassYear_Class.setText(selected_row_data[2])
            
    def populateTextEditsForSubject(self, row, col):
        selected_row_data = []
        for col_idx in range(self.tableWidget_STD_3.columnCount()):
            item = self.tableWidget_STD_3.item(row, col_idx)
            if item is not None:
                selected_row_data.append(item.text())

        # Điền dữ liệu vào các textEdit tương ứng
        if len(selected_row_data) >= 3:
            self.getSubjectID_Sub.setText(selected_row_data[0])
            self.getSubName_Sub.setText(selected_row_data[1])
            self.getUnitstID_Sub.setText(selected_row_data[2])
            
    def populateTextEditsForGrades(self, row, col):
        selected_row_data = []
        for col_idx in range(self.tableWidget_STD_6.columnCount()):
            item = self.tableWidget_STD_6.item(row, col_idx)
            if item is not None:
                selected_row_data.append(item.text())

        # Điền dữ liệu vào các textEdit tương ứng
        if len(selected_row_data) >= 3:
            self.getStudentID_Grades.setText(selected_row_data[0])
            self.getSubjectID_Grades.setText(selected_row_data[1])
            self.getGrades_Grades.setText(selected_row_data[2])
    
    def refreshTableWidget(self, table_name, table_widget):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Xác định tên bảng và cột ID tương ứng
        if table_name == "Student":
            id_column = "StudentID"
        elif table_name == "Classes":
            id_column = "ClassID"
        elif table_name == "Subject":
            id_column = "SubjectID"
        elif table_name == "StudentGrades":
            id_column = "StudentID"
        else:
            raise ValueError("Bảng không hợp lệ")

        # Thực hiện truy vấn để lấy dữ liệu từ bảng
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()

        # Xóa tất cả dữ liệu hiện có trong tableWidget
        table_widget.setRowCount(0)

        # Điền dữ liệu mới vào tableWidget
        table_widget.setRowCount(len(data))
        for row_idx, row_data in enumerate(data):
            for col_idx, cell_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(cell_data))
                table_widget.setItem(row_idx, col_idx, item)

        # Đóng kết nối đến cơ sở dữ liệu SQLite
        conn.close()
        
        def set_table_read_only(table_widget):
            for row in range(table_widget.rowCount()):
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        
        set_table_read_only(self.tableWidget_STD)
        set_table_read_only(self.tableWidget_STD_2)
        set_table_read_only(self.tableWidget_STD_3)
        set_table_read_only(self.tableWidget_STD_6)
    
        # Áp dụng màu xám kẻ cho các hàng
        for row_idx in range(self.tableWidget_STD.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD.columnCount()):
                    item = self.tableWidget_STD.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
                    
        for row_idx in range(self.tableWidget_STD_2.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_2.columnCount()):
                    item = self.tableWidget_STD_2.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
                    
        for row_idx in range(self.tableWidget_STD_3.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_3.columnCount()):
                    item = self.tableWidget_STD_3.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
                    
        for row_idx in range(self.tableWidget_STD_6.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_6.columnCount()):
                    item = self.tableWidget_STD_6.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
    
    
    #Student   
    def insertStudent(self):
        student_id = self.getStudentID_STD.text()
        student_name = self.getStudentName_STD.text()
        student_address = self.getStudentAddress_STD.text()
        class_id = self.getClassID_STD.text()
        
        # Kiểm tra xem không có trường nào để trống
        if not student_id or not student_name or not student_address or not class_id:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn thêm học sinh này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            # Thực hiện chức năng Insert
            try:
                cursor.execute("INSERT INTO Student (StudentID, StudentName, StudentAddress, ClassID) VALUES (?, ?, ?, ?)",
                            (student_id, student_name, student_address, class_id))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Thêm học sinh thành công.")
                
                self.refreshTableWidget("Student", self.tableWidget_STD)            

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi thêm học sinh: " + str(e))
            finally:
                conn.close()
    def updateStudent(self):
            student_id = self.getStudentID_STD.text()
            student_name = self.getStudentName_STD.text()
            student_address = self.getStudentAddress_STD.text()
            class_id = self.getClassID_STD.text()
            
             # Kiểm tra xem không có trường nào để trống
            if not student_id or not student_name or not student_address or not class_id:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
                return
            

            base_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(base_dir, 'dataBase/smdb.db')

            # Kết nối đến cơ sở dữ liệu SQLite
            conn = sqlite3.connect(db_path)
            conn.execute('PRAGMA foreign_keys = ON')
            cursor = conn.cursor()
            confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn cập nhật thông tin học sinh này?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if confirm == QtWidgets.QMessageBox.Yes:
                # Thực hiện chức năng Update
                try:
                    cursor.execute("UPDATE Student SET StudentName = ?, StudentAddress = ?, ClassID = ? WHERE StudentID = ?",
                                (student_name, student_address, class_id, student_id))
                    conn.commit()
                    QtWidgets.QMessageBox.information(self, "Thông báo", "Cập nhật thông tin học sinh thành công.")

                    self.refreshTableWidget("Student", self.tableWidget_STD)


                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi cập nhật thông tin học sinh: " + str(e))
                finally:
                    conn.close()  
    def deleteStudent(self):
        student_id = self.getStudentID_STD.text()
        
        # Kiểm tra xem không có trường nào để trống
        if not student_id:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xoá học sinh này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            # Thực hiện chức năng Delete
            try:
                cursor.execute("DELETE FROM Student WHERE StudentID = ?", (student_id,))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Xóa học sinh thành công.")

                self.refreshTableWidget("Student", self.tableWidget_STD)

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi xóa học sinh: " + str(e))
            finally:
                conn.close()
    def clearStudent(self):
        self.getStudentID_STD.clear()
        self.getStudentName_STD.clear()
        self.getStudentAddress_STD.clear()
        self.getClassID_STD.clear()
    def searchStudent(self):
        student_id = self.getStudentID_STD.text()
        student_name = self.getStudentName_STD.text()
        student_address = self.getStudentAddress_STD.text()
        class_id = self.getClassID_STD.text()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()


        # Xây dựng câu truy vấn SQL dựa trên dữ liệu nhập vào
        query = "SELECT * FROM Student WHERE 1"
        if student_id:
            query += f" AND StudentID = '{student_id}'"
        if student_name:
            query += f" AND StudentName LIKE '%{student_name}%'"
        if student_address:
            query += f" AND StudentAddress LIKE '%{student_address}%'"
        if class_id:
            query += f" AND ClassID LIKE '%{class_id}%'"

        try:
            # Thực hiện truy vấn SQL
            cursor.execute(query)
            data = cursor.fetchall()

            # Xóa tất cả dữ liệu hiện có trong tableWidget_STD
            self.tableWidget_STD.setRowCount(0)

            # Điền dữ liệu mới vào tableWidget_STD
            self.tableWidget_STD.setRowCount(len(data))
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(cell_data))
                    self.tableWidget_STD.setItem(row_idx, col_idx, item)

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi tìm kiếm học sinh: " + str(e))
        finally:
            conn.close()
            
        def set_table_read_only(table_widget):
            for row in range(table_widget.rowCount()):
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        
        set_table_read_only(self.tableWidget_STD)

        for row_idx in range(self.tableWidget_STD.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD.columnCount()):
                    item = self.tableWidget_STD.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
    #Classes
    def insertClasses(self):
        class_id = self.getClassID_Class.text()
        class_name = self.getClassName_Class.text()
        class_year = self.getClassYear_Class.text()
        
         # Kiểm tra xem không có trường nào để trống
        if not class_id or not class_name or not class_year or not class_id:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn thêm lớp này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            # Thực hiện chức năng Insert
            try:
                cursor.execute("INSERT INTO Classes (ClassID, ClassName, ClassYear) VALUES (?, ?, ?)",
                            (class_id, class_name, class_year))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Thêm Lớp thành công.")
                
                self.refreshTableWidget("Classes", self.tableWidget_STD_2)            

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi thêm lớp: " + str(e))
            finally:
                conn.close()  
    def updateClasses(self):
        class_id = self.getClassID_Class.text()
        class_name = self.getClassName_Class.text()
        class_year = self.getClassYear_Class.text()
        
         # Kiểm tra xem không có trường nào để trống
        if not class_id or not class_name or not class_year or not class_id:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn cập nhật thông tin lớp này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            # Thực hiện chức năng Update
            try:
                cursor.execute("UPDATE Classes SET ClassName = ?, ClassYear = ? WHERE ClassID = ?",
                            (class_name, class_year, class_id))
                
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Cập nhật thông tin lớp thành công.")

                self.refreshTableWidget("Classes", self.tableWidget_STD_2)


            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi cập nhật thông tin lớp: " + str(e))
            finally:
                conn.close()   
    def deleteClasses(self):
        class_id = self.getClassID_Class.text()
        
         # Kiểm tra xem không có trường nào để trống
        if not class_id:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xoá lớp này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
        # Thực hiện chức năng Delete
            try:
                cursor.execute("DELETE FROM Classes WHERE ClassID = ?", (class_id,))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Xóa lớp thành công.")

                self.refreshTableWidget("Classes", self.tableWidget_STD_2)

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi xóa lớp: " + str(e))
            finally:
                conn.close()
    def clearClasses(self):
        self.getClassID_Class.clear()
        self.getClassName_Class.clear()
        self.getClassYear_Class.clear()
    def searchClasses(self):
        class_id = self.getClassID_Class.text()
        class_name = self.getClassName_Class.text()
        class_year = self.getClassYear_Class.text()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()


        # Xây dựng câu truy vấn SQL dựa trên dữ liệu nhập vào
        query = "SELECT * FROM Classes WHERE 1"
        if class_id:
            query += f" AND ClassID = '{class_id}'"
        if class_name:
            query += f" AND ClassName LIKE '%{class_name}%'"
        if class_year:
            query += f" AND ClassYear LIKE '%{class_year}%'"

        try:
            # Thực hiện truy vấn SQL
            cursor.execute(query)
            data = cursor.fetchall()

            # Xóa tất cả dữ liệu hiện có trong tableWidget_STD_2
            self.tableWidget_STD_2.setRowCount(0)

            # Điền dữ liệu mới vào tableWidget_STD_2
            self.tableWidget_STD_2.setRowCount(len(data))
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(cell_data))
                    self.tableWidget_STD_2.setItem(row_idx, col_idx, item)

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi tìm kiếm lớp: " + str(e))
        finally:
            conn.close()
            
        def set_table_read_only(table_widget):
            for row in range(table_widget.rowCount()):
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        
        set_table_read_only(self.tableWidget_STD_2)
    #Subject
    def insertSubject(self):
        subject_id = self.getSubjectID_Sub.text()
        subject_name = self.getSubName_Sub.text()
        units = self.getUnitstID_Sub.text()
        
         # Kiểm tra xem không có trường nào để trống
        if not subject_id or not subject_name or not units:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn thêm môn học này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            # Thực hiện chức năng Insert
            try:
                cursor.execute("INSERT INTO Subject (SubjectID, SubjectName, Units) VALUES (?, ?, ?)",
                            (subject_id, subject_name, units))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Thêm môn học thành công.")
                
                self.refreshTableWidget("Subject", self.tableWidget_STD_3)            

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi thêm môn học: " + str(e))
            finally:
                conn.close()   
    def updateSubject(self):
        subject_id = self.getSubjectID_Sub.text()
        subject_name = self.getSubName_Sub.text()
        units = self.getUnitstID_Sub.text()
        
        if not subject_id or not subject_name or not units:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return


        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn cập nhật thông môn học này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            # Thực hiện chức năng Update
            try:
                cursor.execute("UPDATE Subject SET SubjectName = ?, Units = ? WHERE SubjectID = ?",
                            (subject_name, units, subject_id))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Cập nhật thông tin môn học thành công.")

                self.refreshTableWidget("Subject", self.tableWidget_STD_3)


            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi cập nhật thông tin môn học: " + str(e))
            finally:
                conn.close()      
    def deleteSubject(self):
        subject_id = self.getSubjectID_Sub.text()
        
        if not subject_id:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xoá môn học này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
        # Thực hiện chức năng Delete
            try:
                cursor.execute("DELETE FROM Subject WHERE SubjectID = ?", (subject_id,))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Xóa môn học thành công.")

                self.refreshTableWidget("Subject", self.tableWidget_STD_3)

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi xóa môn học: " + str(e))
            finally:
                conn.close()
    def clearSubject(self):
        self.getSubjectID_Sub.clear()
        self.getSubName_Sub.clear()
        self.getUnitstID_Sub.clear()   
    def searchSubject(self):
        subject_id = self.getSubjectID_Sub.text()
        subject_name = self.getSubName_Sub.text()
        units = self.getUnitstID_Sub.text()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()


        # Xây dựng câu truy vấn SQL dựa trên dữ liệu nhập vào
        query = "SELECT * FROM Subject WHERE 1"
        if subject_id:
            query += f" AND SubjectID = '{subject_id}'"
        if subject_name:
            query += f" AND SubjectName LIKE '%{subject_name}%'"
        if units:
            query += f" AND Units LIKE '%{units}%'"

        try:
            # Thực hiện truy vấn SQL
            cursor.execute(query)
            data = cursor.fetchall()

            # Xóa tất cả dữ liệu hiện có trong tableWidget_STD_3
            self.tableWidget_STD_3.setRowCount(0)

            # Điền dữ liệu mới vào tableWidget_STD_3
            self.tableWidget_STD_3.setRowCount(len(data))
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(cell_data))
                    self.tableWidget_STD_3.setItem(row_idx, col_idx, item)

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi tìm kiếm môn học: " + str(e))
        finally:
            conn.close()
            
        def set_table_read_only(table_widget):
            for row in range(table_widget.rowCount()):
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        
        set_table_read_only(self.tableWidget_STD_3)
        
        for row_idx in range(self.tableWidget_STD_3.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_3.columnCount()):
                    item = self.tableWidget_STD_3.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
    #Grades
    def insertGrades(self):
        studentID = self.getStudentID_Grades.text()
        subjectID = self.getSubjectID_Grades.text()
        grades = self.getGrades_Grades.text()
        
        if not studentID or not subjectID or not grades:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')
        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn thêm điểm cho học sinh?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
            # Thực hiện chức năng Insert
            try:
                cursor.execute("INSERT INTO StudentGrades (StudentID, SubjectID, Grades) VALUES (?, ?, ?)",
                            (studentID, subjectID, grades))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Thêm điểm cho học sinh thành công.")
                
                self.refreshTableWidget("StudentGrades", self.tableWidget_STD_6)            

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi thêm điểm cho học sinh: " + str(e))
            finally:
                conn.close()   
    def updateGrades(self):
            studentID = self.getStudentID_Grades.text()
            subjectID = self.getSubjectID_Grades.text()
            grades = self.getGrades_Grades.text()
            
            if not studentID or not subjectID or not grades:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
                return

            base_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(base_dir, 'dataBase/smdb.db')

            # Kết nối đến cơ sở dữ liệu SQLite
            conn = sqlite3.connect(db_path)
            conn.execute('PRAGMA foreign_keys = ON')
            cursor = conn.cursor()
            confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn cập nhật điểm cho học sinh này?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if confirm == QtWidgets.QMessageBox.Yes:
                # Thực hiện chức năng Update
                try:
                    cursor.execute("UPDATE StudentGrades SET Grades = ? WHERE StudentID = ? AND SubjectID = ?",
                                            (grades, studentID, subjectID))
                    conn.commit()
                    QtWidgets.QMessageBox.information(self, "Thông báo", "Cập nhật thông tin điểm cho học sinh thành công.")

                    self.refreshTableWidget("StudentGrades", self.tableWidget_STD_6)


                except sqlite3.Error as e:
                    QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi cập nhật điểm cho học sinh: " + str(e))
                finally:
                    conn.close()         
    def deleteGrades(self):
        studentID = self.getStudentID_Grades.text()
        subjectID = self.getSubjectID_Grades.text()
        
        if not studentID or not subjectID:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng điền đầy đủ thông tin.")
            return
        

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        conn.execute('PRAGMA foreign_keys = ON')
        cursor = conn.cursor()
        confirm = QtWidgets.QMessageBox.question(self, "Xác nhận", "Bạn có chắc chắn muốn xoá điểm cho học sinh này?",
                                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if confirm == QtWidgets.QMessageBox.Yes:
        # Thực hiện chức năng Delete
            try:
                cursor.execute("DELETE FROM StudentGrades WHERE StudentID = ? AND SubjectID = ?", (studentID,subjectID))
                conn.commit()
                QtWidgets.QMessageBox.information(self, "Thông báo", "Xóa điểm cho học sinh thành công.")

                self.refreshTableWidget("StudentGrades", self.tableWidget_STD_6)

            except sqlite3.Error as e:
                QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi xóa điểm cho học sinh: " + str(e))
            finally:
                conn.close()
    def clearGrades(self):
        self.getStudentID_Grades.clear()
        self.getSubjectID_Grades.clear()
        self.getGrades_Grades.clear()   
    def searchGrades(self):
        studentID = self.getStudentID_Grades.text()
        subjectID = self.getSubjectID_Grades.text()
        grades = self.getGrades_Grades.text()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, 'dataBase/smdb.db')

        # Kết nối đến cơ sở dữ liệu SQLite
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()


        # Xây dựng câu truy vấn SQL dựa trên dữ liệu nhập vào
        query = "SELECT * FROM StudentGrades WHERE 1"
        if studentID:
            query += f" AND StudentID = '{studentID}'"
        if subjectID:
            query += f" AND SubjectID LIKE '%{subjectID}%'"
        if grades:
            query += f" AND Grades LIKE '%{grades}%'"

        try:
            # Thực hiện truy vấn SQL
            cursor.execute(query)
            data = cursor.fetchall()

            # Xóa tất cả dữ liệu hiện có trong tableWidget_STD_6
            self.tableWidget_STD_6.setRowCount(0)

            # Điền dữ liệu mới vào tableWidget_STD_6
            self.tableWidget_STD_6.setRowCount(len(data))
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(cell_data))
                    self.tableWidget_STD_6.setItem(row_idx, col_idx, item)

        except sqlite3.Error as e:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Lỗi khi tìm kiếm điểm học sinh: " + str(e))
        finally:
            conn.close()
            
        def set_table_read_only(table_widget):
            for row in range(table_widget.rowCount()):
                for col in range(table_widget.columnCount()):
                    item = table_widget.item(row, col)
                    if item is not None:
                        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
        
        set_table_read_only(self.tableWidget_STD_6)
        
        for row_idx in range(self.tableWidget_STD_6.rowCount()):
            if row_idx % 2 == 0:
                # Đặt màu nền cho hàng chẵn
                for col_idx in range(self.tableWidget_STD_6.columnCount()):
                    item = self.tableWidget_STD_6.item(row_idx, col_idx)
                    item.setBackground(QtGui.QColor(235, 240, 236))
    
    #stu
    def sortTableStu(self):
            selected_column = self.comboBox_sortBy_Std.currentIndex()
            order_index = self.comboBox_orderBy_Std.currentIndex()
        
            if order_index == 0:
                order = QtCore.Qt.AscendingOrder
            else:
                order = QtCore.Qt.DescendingOrder

            self.tableWidget_STD.sortItems(selected_column, order) 
    def resetTableStu(self):
        self.comboBox_sortBy_Std.setCurrentIndex(0)  
        self.comboBox_orderBy_Std.setCurrentIndex(0) 


        self.tableWidget_STD.setSortingEnabled(True) 
        self.tableWidget_STD.sortItems(0, QtCore.Qt.AscendingOrder)  
        self.tableWidget_STD.setSortingEnabled(False)
    #class
    def sortTableClass(self):
            selected_column = self.comboBox_sortBy_Class.currentIndex()
            order_index = self.comboBox_orderBy_Class.currentIndex()
        
            if order_index == 0:
                order = QtCore.Qt.AscendingOrder
            else:
                order = QtCore.Qt.DescendingOrder

            self.tableWidget_STD_2.sortItems(selected_column, order) 
    def resetTableClass(self):
        self.comboBox_orderBy_Class.setCurrentIndex(0)  
        self.comboBox_orderBy_Class.setCurrentIndex(0) 


        self.tableWidget_STD_2.setSortingEnabled(True) 
        self.tableWidget_STD_2.sortItems(0, QtCore.Qt.AscendingOrder)  
        self.tableWidget_STD_2.setSortingEnabled(False)
    #sub   
    def sortTableSub(self):
            selected_column = self.comboBox_sortBy_Sub.currentIndex()
            order_index = self.comboBox_orderBy_sub.currentIndex()
        
            if order_index == 0:
                order = QtCore.Qt.AscendingOrder
            else:
                order = QtCore.Qt.DescendingOrder

            self.tableWidget_STD_3.sortItems(selected_column, order) 
    def resetTableSub(self):
        self.comboBox_sortBy_Sub.setCurrentIndex(0)  
        self.comboBox_orderBy_sub.setCurrentIndex(0) 


        self.tableWidget_STD_3.setSortingEnabled(True) 
        self.tableWidget_STD_3.sortItems(0, QtCore.Qt.AscendingOrder)  
        self.tableWidget_STD_3.setSortingEnabled(False)    
    #grades        
    def sortTableGrades(self):
            selected_column = self.comboBox_sortBy_stuGra.currentIndex()
            order_index = self.comboBox_orderBy_stdGra.currentIndex()
        
            if order_index == 0:
                order = QtCore.Qt.AscendingOrder
            else:
                order = QtCore.Qt.DescendingOrder

            self.tableWidget_STD_6.sortItems(selected_column, order) 
    def resetTableGrades(self):
        self.comboBox_sortBy_stuGra.setCurrentIndex(0)  
        self.comboBox_orderBy_stdGra.setCurrentIndex(0) 


        self.tableWidget_STD_6.setSortingEnabled(True) 
        self.tableWidget_STD_6.sortItems(0, QtCore.Qt.AscendingOrder)  
        self.tableWidget_STD_6.setSortingEnabled(False)       
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    sys.exit(app.exec_())