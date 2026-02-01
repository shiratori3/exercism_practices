import io


class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""

    def __init__(self, file_obj=None):
        if file_obj is None:
            file_obj = io.BytesIO()
        super().__init__(file_obj)
        self.cnt_write_ops = 0
        self.cnt_read_ops = 0
        self.cnt_bytes_write = 0
        self.cnt_bytes_read = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return super().__exit__(exc_type, exc_val, exc_tb)

    def __iter__(self):
        return self

    def __next__(self):
        line = super().readline()
        if line:
            self.cnt_read_ops += 1
            self.cnt_bytes_read += len(line)
            return line
        raise StopIteration

    def read(self, size=-1):
        data = super().read(size)
        n = len(data)
        self.cnt_read_ops += 1
        self.cnt_bytes_read += n
        return data

    @property
    def read_bytes(self):
        return self.cnt_bytes_read

    @property
    def read_ops(self):
        return self.cnt_read_ops

    def write(self, b):
        n = super().write(b)
        self.cnt_write_ops += 1
        self.cnt_bytes_write += n
        return n

    @property
    def write_bytes(self):
        return self.cnt_bytes_write

    @property
    def write_ops(self):
        return self.cnt_write_ops


class MeteredSocket:
    """Implement using a delegation model."""

    def __init__(self, socket):
        self._socket = socket
        self.cnt_send_ops = 0
        self.cnt_recv_ops = 0
        self.cnt_bytes_send = 0
        self.cnt_bytes_recv = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._socket.__exit__(exc_type, exc_val, exc_tb)

    def recv(self, bufsize, flags=0):
        data = self._socket.recv(bufsize, flags)
        self.cnt_recv_ops += 1
        self.cnt_bytes_recv += len(data)
        return data

    @property
    def recv_bytes(self):
        return self.cnt_bytes_recv

    @property
    def recv_ops(self):
        return self.cnt_recv_ops

    def send(self, data, flags=0):
        n = self._socket.send(data, flags)
        self.cnt_send_ops += 1
        self.cnt_bytes_send += n
        return n

    @property
    def send_bytes(self):
        return self.cnt_bytes_send

    @property
    def send_ops(self):
        return self.cnt_send_ops
