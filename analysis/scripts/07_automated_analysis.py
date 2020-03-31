import time
import threading
# Don't put numbers in your file names guys
run_selected_frame = __import__('analysis.scripts.03_download_report.run_selected_frame')
run_analysis_for_all = __import__('analysis.scripts.05_script_analysis.run_analysis_for_all')
export_daily_report_to_csv = __import__('analysis.scripts.06_export_csv.export_daily_report_to_csv')


def automated_analysis(end_event: threading.Event, refresh_time: float=3600):
    flag_failed = False

    while True:
        try:
            print('Launching analysis...')

            run_selected_frame()
            print('Downloaded reports')

            run_analysis_for_all(10000)
            print('Analysed reports')

            export_daily_report_to_csv()
            print('Exported reports')
            print(time.ctime())

        except ...:
            print('Analysis failed! Restarting...')
            flag_failed = True

        if not flag_failed:
            quit = end_event.wait(refresh_time)
            if quit:
                print('Terminating automated analysis...')
                break
        else:
            # Reset flag
            flag_failed = False


if __name__ == '__main__':

    wait_time = 3600
    event_quit = threading.Event()

    analysis_thread = threading.Thread(target=automated_analysis, args=[event_quit, wait_time])
    analysis_thread.start()

    stop_char = ''
    while stop_char.lower() != 'q':
        stop_char = input('\nEnter \'q\' to quit automated analysis.\n')

    event_quit.set()
    analysis_thread.join()

