
# quaternions.py
# Простая реализация кватернионов и операций с ними

import math

class Quaternion:
    def __init__(self, w, x, y, z):
        self.w = float(w)
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __repr__(self):
        return f"Quaternion({self.w}, {self.x}, {self.y}, {self.z})"

    def as_tuple(self):
        return (self.w, self.x, self.y, self.z)

    def norm(self):
        return math.sqrt(self.w*self.w + self.x*self.x + self.y*self.y + self.z*self.z)

    def normalized(self):
        n = self.norm()
        if n == 0:
            raise ZeroDivisionError("Cannot normalize zero quaternion")
        return Quaternion(self.w/n, self.x/n, self.y/n, self.z/n)

    def conjugate(self):
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def inverse(self):
        n2 = self.w*self.w + self.x*self.x + self.y*self.y + self.z*self.z
        if n2 == 0:
            raise ZeroDivisionError("Inverse of zero quaternion")
        c = self.conjugate()
        return Quaternion(c.w/n2, c.x/n2, c.y/n2, c.z/n2)

    def __mul__(self, other):
        # Гамильтоново умножение кватернионов
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        w = w1*w2 - x1*x2 - y1*y2 - z1*z2
        x = w1*x2 + x1*w2 + y1*z2 - z1*y2
        y = w1*y2 - x1*z2 + y1*w2 + z1*x2
        z = w1*z2 + x1*y2 - y1*x2 + z1*w2
        return Quaternion(w, x, y, z)

    def rotate_vector(self, v):
        # v — кортеж/список (vx, vy, vz)
        qv = Quaternion(0, v[0], v[1], v[2])
        q_res = self * qv * self.inverse()
        return (q_res.x, q_res.y, q_res.z)

    def to_rotation_matrix(self):
        # Возвращает 3x3 матрицу вращения как кортеж строк
        w, x, y, z = self.w, self.x, self.y, self.z
        # Предполагается, что кватернион нормирован; при необходимости нормализуйте заранее
        xx = x*x; yy = y*y; zz = z*z
        xy = x*y; xz = x*z; yz = y*z
        wx = w*x; wy = w*y; wz = w*z
        m00 = 1 - 2*(yy + zz)
        m01 = 2*(xy - wz)
        m02 = 2*(xz + wy)
        m10 = 2*(xy + wz)
        m11 = 1 - 2*(xx + zz)
        m12 = 2*(yz - wx)
        m20 = 2*(xz - wy)
        m21 = 2*(yz + wx)
        m22 = 1 - 2*(xx + yy)
        return ((m00, m01, m02),
                (m10, m11, m12),
                (m20, m21, m22))

    @staticmethod
    def from_axis_angle(axis, angle_rad):
        # axis — (ax, ay, az), может быть не нормирован
        ax, ay, az = axis
        norm = math.sqrt(ax*ax + ay*ay + az*az)
        if norm == 0:
            raise ValueError("Axis must be non-zero")
        ux, uy, uz = ax/norm, ay/norm, az/norm
        half = angle_rad / 2.0
        s = math.sin(half)
        return Quaternion(math.cos(half), ux*s, uy*s, uz*s)

    @staticmethod
    def from_rotation_matrix(m):
        # m — 3x3 матрица (последовательность 3-х строк)
        m00, m01, m02 = m[0]
        m10, m11, m12 = m[1]
        m20, m21, m22 = m[2]
        trace = m00 + m11 + m22
        if trace > 0:
            s = math.sqrt(trace + 1.0) * 2  # s = 4*w
            w =0.25 * s
            x = (m21 - m12) / s
            y = (m02 - m20) / s
            z = (m10 - m01) / s
        else:
            if (m00 > m11) and (m00 > m22):
                s = math.sqrt(1.0 + m00 - m11 - m22) * 2  # s = 4*x
                w = (m21 - m12) / s
                x = 0.25 * s
                y = (m01 + m10) / s
                z = (m02 + m20) / s
            elif m11 > m22:
                s = math.sqrt(1.0 + m11 - m00 - m22) * 2  # s = 4*y
                w = (m02 - m20) / s
                x = (m01 + m10) / s
                y = 0.25 * s
                z = (m12 + m21) / s
            else:
                s = math.sqrt(1.0 + m22 - m00 - m11) * 2  # s = 4*z
                w = (m10 - m01) / s
                x = (m02 + m20) / s
                y = (m12 + m21) / s
                z = 0.25 * s
        return Quaternion(w, x, y, z).normalized()

# Пример использования
if __name__ == "__main__":
    # Поворот 90 градусов вокруг оси z
    q = Quaternion.from_axis_angle((0,0,1), math.pi/2).normalized()
    v = (1, 0, 0)
    v_rot = q.rotate_vector(v)
    print("q =", q)
    print("v rotated =", v_rot)  # ожидается (0, 1, 0) (в пределах численной погрешности)

    # Конвертация в матрицу
    R = q.to_rotation_matrix()
    print("Rotation matrix:")
    for row in R:
        print(row)

    # Композиция поворотов: сначала q1 затем q2 => q_total = q2 * q1
    q1 = Quaternion.from_axis_angle((1,0,0), math.radians(30)).normalized()
    q2 = Quaternion.from_axis_angle((0,1,0), math.radians(45)).normalized()
    q_total = q2 * q1
    print("Composite quaternion:", q_total.normalized())
