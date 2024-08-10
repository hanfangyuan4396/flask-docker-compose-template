gunicorn -w ${WORKER_NUM} --access-logfile - --error-logfile - app:app -b 0.0.0.0:${PORT} 2>&1 | tee -a gunicorn.log
# 使用preload参数只启动一次主进程，共享内存
# gunicorn -w ${WORKER_NUM} --access-logfile - --error-logfile - --preload app:app -b 0.0.0.0:${PORT} 2>&1 | tee -a gunicorn.log