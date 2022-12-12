import sys
import subprocess as sp
import validators as vals

def is_reachable(host, sz=None):
    args = ["ping", host, "-c", "3"]
    if sz:
        args.extend(["-M", "do", "-s", str(sz)])

    p = sp.run(args, stdout=sp.DEVNULL, stderr=sp.DEVNULL)

    return p.returncode == 0

def main():
    if len(sys.argv) != 2:
        print("Exactly one argument required: host", file=sys.stderr)
        exit(1)

    host = sys.argv[1]
    if not vals.domain(host) and not vals.ip_address.ipv4(host):
        print("Invalid host", file=sys.stderr)
        exit(1)

    if int(sp.check_output(["cat", "/proc/sys/net/ipv4/icmp_echo_ignore_all"])) != 0:
        print("ICMP is blocked")
        exit(1)

    if not is_reachable(host):
        print("Host unreachable", file=sys.stderr)
        exit(1)

    # ищем path mtu бин поиском
    l = -1
    r = 10000 # проверяем на jumbo фреймы с запасом
    while l < r - 1:
        m = (l + r) // 2
        if is_reachable(host, m):
            l = m
        else:
            r = m
    print(l + 28) # не забываем размеры ip и icmp хедеров

if __name__ == "__main__":
    main()
