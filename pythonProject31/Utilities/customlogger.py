import logging


class LogGen:
    @staticmethod
    def loggen():

        logging.basicConfig(
            filename="C:\\Users\\Chetan Ramesh\\PycharmProjects\\CompleteTestcase\\Logs\\automation.log,"
                     "format='%(levelness)s:   %(Pastime)s:   %(message)s',"
                     "datefmt='%m/ %d/ %Y  %I: %M  %S  %p' , level = logging.INFO, force=True")

        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='C:\\Users\\Chetan Ramesh\\PycharmProjects\\pythonProject31\\Logs'
                                                '\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)

        logger.setLevel(logging.INFO)
        logger.info("This is INFO Log")
        return logger
