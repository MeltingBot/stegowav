from pathlib import Path

from evaluation.report_analysis.eval_report_analyzer import EvalReportAnalyzer
from evaluation.report_analysis.csv_reader import CsvReader
from evaluation.report_analysis.visualizer import EvalReportVisualizer


def main():

    eval_reports_path = Path('eval_reports')
    graphs_path = 'report_graphs'

    Path(graphs_path).mkdir(parents=True, exist_ok=True)

    csv_reader = CsvReader(eval_reports_path)
    eval_reports = csv_reader.read_all_eval_reports()

    analyzer = EvalReportAnalyzer(eval_reports)

    choices_per_files = analyzer.get_choices_per_file_pair()
    results_per_files = analyzer.get_results_per_file_pair()

    visualizer = EvalReportVisualizer()
    visualizer.draw_pandas_barh_for_each_file(choices_per_files, graphs_path, 'choices')
    visualizer.draw_pandas_barh_for_each_file(results_per_files, graphs_path, 'results')


if __name__ == "__main__":
    main()
