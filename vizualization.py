import os
import logging
import matplotlib.pyplot as plt

logger = logging.getLogger()
logger.setLevel("INFO")


def visualize_statistics(statistics: dict, visual_directory: str) -> None:
    fig = plt.figure(figsize=(25, 15))
    plt.rcParams["font.size"] = "24"
    plt.ylabel("Время работы, с", fontsize=24)
    plt.xlabel("Количество процессов", fontsize=24)
    plt.title("График зависимости времени от количества процессов", fontsize=40)
    pools, work_times = statistics.keys(), statistics.values()
    plt.bar(pools, work_times, color="maroon", width=0.7)
    plt.savefig(os.path.join(visual_directory, "statistics.png"))
    logging.info(f'График сохранен в папку "{visual_directory}"')
