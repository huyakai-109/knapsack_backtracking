import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_knapsack import Ui_MainWindow
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def backtracking(values, weights, max_weight):
    values = [float(val) for val in values.split(',')]
    weights = [float(wt) for wt in weights.split(',')]
    max_weight = float(max_weight)

    total_items = len(values)
    max_val = 0
    best_weight = 0
    best_set = None
    current_option = [0] * total_items
    all_sets = []
    all_values = []
    all_weights = []

    def backtrack(i, current_value, current_weight):
        nonlocal max_val, best_set, best_weight
        if current_weight > max_weight:
            return
        if i == total_items:
            if current_value > max_val:
                max_val = current_value
                best_set = current_option[:]
                best_weight = current_weight
                all_sets.append(current_option[:])
                all_values.append(current_value)
                all_weights.append(current_weight)
        else:
            current_option[i] = 1
            backtrack(i + 1, current_value +
                    values[i], current_weight + weights[i])
            current_option[i] = 0
            backtrack(i + 1, current_value, current_weight)

    backtrack(0, 0, 0)
    return max_val, best_set, best_weight, all_sets, all_values, all_weights


class KnapsackApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Knapsack Problem Solver')

        self.random_button.clicked.connect(self.random_data)
        self.solve_button.clicked.connect(self.solve_knapsack)
        self.show_button.clicked.connect(self.show_pic)

    def solve_knapsack(self):
        values = self.values_input.text()
        weights = self.weights_input.text()
        max_weight = self.max_weight_input.text()

        try:
            if values and weights and max_weight:
                max_val, best_set, best_weight, all_sets, all_values, all_weights = backtracking(
                    values, weights, max_weight)
                self.result_label.setText(
                    f"Giá trị lớn nhất của túi: {max_val}\nCác sản phẩm trong túi: {best_set}\nKhối lượng hiện tại là: {best_weight}\nAll set: {all_sets}")
            else:
                self.result_label.setText("Không được bỏ trống")
        except ValueError:
            self.result_label.setText("Sai dữ liệu")

    def random_data(self):
        import random

        values = [random.randint(1, 10) for i in range(6)]
        weights = [random.randint(1, 10) for i in range(6)]

        max_weight = 15

        self.values_input.setText(','.join(str(val) for val in values))
        self.weights_input.setText(','.join(str(wt) for wt in weights))
        self.max_weight_input.setText(str(max_weight))

    def show_pic(self):
        values = self.values_input.text()
        weights = self.weights_input.text()
        max_weight = self.max_weight_input.text()
        if values and weights and max_weight:
            max_val, best_set, best_weight, all_sets, all_values, all_weights = backtracking(
                values, weights, max_weight)
            stt = list(range(1, len(all_values) + 1))

        # Create subplots
            fig = make_subplots(rows=1, cols=2, subplot_titles=(
                'Biểu đồ thay đổi khối lượng', 'Biểu đồ thay đổi giá trị'))

        # Add scatter plots to subplots
            fig.add_trace(go.Scatter(x=stt, y=all_weights,
                                    mode='lines+markers', name='Khối lượng'), row=1, col=1)
            fig.add_trace(go.Scatter(x=stt, y=all_values,
                                    mode='lines+markers', name='Giá trị'), row=1, col=2)

        # Find the maximum point on the charts
            max_weight_index = all_weights.index(max(all_weights))
            max_value_index = all_values.index(max(all_values))

        # Add annotations for maximum points
            fig.add_annotation(
                go.layout.Annotation(
                    text=f'Max Khối lượng: {all_weights[max_weight_index]}',
                    x=max_weight_index + 1,
                    y=all_weights[max_weight_index],
                    showarrow=True,
                    arrowhead=7,
                    ax=20,
                    ay=-30
                ),
                row=1, col=1
            )

            fig.add_annotation(
                go.layout.Annotation(
                    text=f'Max Giá trị: {all_values[max_value_index]}',
                    x=max_value_index + 1,
                    y=all_values[max_value_index],
                    showarrow=True,
                    arrowhead=7,
                    ax=-20,
                    ay=30
                ),
                row=1, col=2
            )

        # Update layout and show the figure
            fig.update_layout(
                title_text="Biểu đồ thay đổi khối lượng và giá trị",
                # xaxis_title="Bước",
                yaxis_title="Khối lượng",
                yaxis2_title="Giá trị"
            )
            fig.show()
        else:
            self.result_label.setText("Không được bỏ trống")


def main():
    app = QApplication(sys.argv)
    window = KnapsackApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
