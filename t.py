import sys
from datetime import datetime, timedelta
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QLabel, QDateTimeEdit,
                             QTableWidget, QGridLayout, QTableWidgetItem, QHeaderView,
                             QFrame, QStackedWidget)
from PyQt6.QtCore import Qt, QDateTime
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QPieSeries, QBarCategoryAxis, QValueAxis
from PyQt6.QtGui import QColor, QPalette, QFont, QIcon


class SidebarButton(QPushButton):
    def __init__(self, icon_path, text=""):
        super().__init__()
        self.setFixedSize(40, 40)
        if icon_path:
            self.setIcon(QIcon(icon_path))
        self.setStyleSheet("""
            QPushButton {
                background-color: #2d2d3f;
                border: none;
                border-radius: 8px;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #3d3d4f;
            }
        """)


class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #1a1a2e;
            }
            QWidget {
                color: white;
            }
            QPushButton {
                background-color: #3f3f5f;
                border: none;
                border-radius: 4px;
                padding: 5px 15px;
                color: white;
            }
            QPushButton:hover {
                background-color: #4f4f6f;
            }
            QTableWidget {
                background-color: #2d2d3f;
                border: none;
                border-radius: 8px;
                gridline-color: #3d3d4f;
            }
            QTableWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #2d2d3f;
                color: white;
                border: none;
                padding: 5px;
            }
            QDateTimeEdit {
                background-color: #2d2d3f;
                border: none;
                border-radius: 4px;
                padding: 5px;
                color: white;
            }
        """)

        # Create main layout with sidebar
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Create sidebar
        sidebar = QWidget()
        sidebar.setFixedWidth(50)
        sidebar.setStyleSheet("background-color: #2d2d3f;")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Add sidebar buttons (you'll need to add actual icons)
        sidebar_buttons = [
            SidebarButton("path_to_dashboard_icon.png"),
            SidebarButton("path_to_orders_icon.png"),
            SidebarButton("path_to_customers_icon.png"),
            SidebarButton("path_to_products_icon.png"),
            SidebarButton("path_to_reports_icon.png")
        ]
        for btn in sidebar_buttons:
            sidebar_layout.addWidget(btn)

        # Create content area
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)

        # Header with date range and buttons
        header = QWidget()
        header_layout = QHBoxLayout(header)

        date_range = QLabel("Feb 16, 2022 - Feb 23, 2022")
        date_range.setStyleSheet("color: #8f8f9f;")

        # Date filter buttons with modern style
        button_style = """
            QPushButton {
                background-color: #3f3f5f;
                border-radius: 15px;
                padding: 5px 15px;
                color: white;
            }
            QPushButton:checked {
                background-color: #6f6fff;
            }
        """

        self.btn_custom = QPushButton("Custom")
        self.btn_today = QPushButton("Today")
        self.btn_last7days = QPushButton("Last 7 days")
        self.btn_last30days = QPushButton("Last 30 days")
        self.btn_this_month = QPushButton("This month")

        for btn in [self.btn_custom, self.btn_today, self.btn_last7days,
                    self.btn_last30days, self.btn_this_month]:
            btn.setStyleSheet(button_style)
            header_layout.addWidget(btn)

        # Create metrics cards
        metrics_widget = QWidget()
        metrics_layout = QHBoxLayout(metrics_widget)

        # Style for metric cards
        card_style = """
            QFrame {
                background-color: #2d2d3f;
                border-radius: 8px;
                padding: 15px;
            }
            QLabel {
                color: white;
            }
        """

        # Orders card
        orders_card = QFrame()
        orders_card.setStyleSheet(card_style)
        orders_layout = QVBoxLayout(orders_card)
        orders_title = QLabel("Orders")
        orders_value = QLabel("53")
        orders_value.setStyleSheet("font-size: 24px; font-weight: bold;")
        orders_percent = QLabel("+15%")
        orders_percent.setStyleSheet("color: #4fff4f;")
        orders_layout.addWidget(orders_title)
        orders_layout.addWidget(orders_value)
        orders_layout.addWidget(orders_percent)

        # Revenue card
        revenue_card = QFrame()
        revenue_card.setStyleSheet(card_style)
        revenue_layout = QVBoxLayout(revenue_card)
        revenue_title = QLabel("Total Revenue")
        revenue_value = QLabel("$82,361.76")
        revenue_value.setStyleSheet("font-size: 24px; font-weight: bold;")
        revenue_percent = QLabel("-23%")
        revenue_percent.setStyleSheet("color: #ff4f4f;")
        revenue_layout.addWidget(revenue_title)
        revenue_layout.addWidget(revenue_value)
        revenue_layout.addWidget(revenue_percent)

        # Profit card
        profit_card = QFrame()
        profit_card.setStyleSheet(card_style)
        profit_layout = QVBoxLayout(profit_card)
        profit_title = QLabel("Total Profit")
        profit_value = QLabel("$16,472.352")
        profit_value.setStyleSheet("font-size: 24px; font-weight: bold;")
        profit_percent = QLabel("+23%")
        profit_percent.setStyleSheet("color: #4fff4f;")
        profit_layout.addWidget(profit_title)
        profit_layout.addWidget(profit_value)
        profit_layout.addWidget(profit_percent)

        metrics_layout.addWidget(orders_card)
        metrics_layout.addWidget(revenue_card)
        metrics_layout.addWidget(profit_card)

        # Create charts section
        charts_widget = QWidget()
        charts_layout = QHBoxLayout(charts_widget)

        # Orders by date chart (area chart)
        self.orders_chart = self.create_orders_chart()
        orders_chart_view = QChartView(self.orders_chart)
        orders_chart_view.setStyleSheet("background-color: #2d2d3f; border-radius: 8px;")
        orders_chart_view.setMinimumHeight(300)

        # Best selling products chart (donut chart)
        self.products_chart = self.create_orders_chart()
        products_chart_view = QChartView(self.products_chart)
        products_chart_view.setStyleSheet("background-color: #2d2d3f; border-radius: 8px;")
        products_chart_view.setMinimumHeight(300)

        charts_layout.addWidget(orders_chart_view, 2)  # 2:1 ratio
        charts_layout.addWidget(products_chart_view, 1)

        # Create bottom section
        bottom_widget = QWidget()
        bottom_layout = QHBoxLayout(bottom_widget)

        # Total counters
        counters_widget = QFrame()
        counters_widget.setStyleSheet(card_style)
        counters_layout = QVBoxLayout(counters_widget)

        counters_title = QLabel("Total Counters")
        counters_layout.addWidget(counters_title)

        counter_items = [
            ("Customers", "91"),
            ("Suppliers", "29"),
            ("Products", "78")
        ]

        for label, value in counter_items:
            item_widget = QWidget()
            item_layout = QHBoxLayout(item_widget)
            item_label = QLabel(label)
            item_value = QLabel(value)
            item_value.setStyleSheet("font-weight: bold;")
            item_layout.addWidget(item_label)
            item_layout.addWidget(item_value)
            counters_layout.addWidget(item_widget)

        # Understock table
        self.understock_table = QTableWidget()
        self.understock_table.setColumnCount(2)
        self.understock_table.setHorizontalHeaderLabels(["Item", "Units"])
        self.understock_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.understock_table.setStyleSheet("""
            QTableWidget {
                background-color: #2d2d3f;
                border-radius: 8px;
                padding: 10px;
            }
        """)

        bottom_layout.addWidget(counters_widget)
        bottom_layout.addWidget(self.understock_table, 2)  # 2:1 ratio

        # Add all sections to content layout
        content_layout.addWidget(header)
        content_layout.addWidget(metrics_widget)
        content_layout.addWidget(charts_widget)
        content_layout.addWidget(bottom_widget)

        # Add sidebar and content to main layout
        main_layout.addWidget(sidebar)
        main_layout.addWidget(content_widget)

        # Load initial data
        self.load_dummy_data()

    def create_orders_chart(self):
        chart = QChart()
        chart.setBackgroundVisible(False)
        chart.setTitle("Orders by date")
        chart.setTitleBrush(QColor("#ffffff"))

        series = QLineSeries()
        series.setColor(QColor("#ff4f8f"))

        chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_y = QValueAxis()
        axis_x.setLabelsColor(QColor("#ffffff"))
        axis_y.setLabelsColor(QColor("#ffffff"))

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        return chart

    def create_orders_chart(self):
        chart = QChart()
        chart.setBackgroundVisible(False)
        chart.setTitle("Orders by date")
        chart.setTitleBrush(QColor("#ffffff"))

        series = QLineSeries()
        series.setColor(QColor("#ff4f8f"))

        # Add the series first
        chart.addSeries(series)

        # Create and configure axes
        axis_x = QBarCategoryAxis()
        axis_x.setLabelsColor(QColor("#ffffff"))

        axis_y = QValueAxis()
        axis_y.setLabelsColor(QColor("#ffffff"))
        axis_y.setRange(0, 20000)

        # Add axes to chart
        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        # Attach axes to series
        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        return chart

    def load_dummy_data(self):
        # Update understock table with dummy data
        understock_data = [
            ("Northwoods Cranberry Sauce", 4),
            ("Queso Cabrales", 3),
            ("Mascarpone Fabioli", 2),
            ("Geitost", 5)
        ]

        self.understock_table.setRowCount(len(understock_data))
        for i, (item, units) in enumerate(understock_data):
            self.understock_table.setItem(i, 0, QTableWidgetItem(item))
            self.understock_table.setItem(i, 1, QTableWidgetItem(str(units)))

        # Update orders chart
        series = QLineSeries()
        dates = ["16 Feb", "17 Feb", "18 Feb", "19 Feb", "20 Feb", "21 Feb", "22 Feb", "23 Feb"]
        values = [8000, 12000, 15000, 10000, 5000, 8000, 16000, 14000]

        for i, (date, value) in enumerate(zip(dates, values)):
            series.append(i, value)

        self.orders_chart.removeAllSeries()
        self.orders_chart.addSeries(series)

        axis_x = QBarCategoryAxis()
        axis_x.append(dates)
        axis_y = QValueAxis()
        axis_y.setRange(0, 20000)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec())