# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

import tensorflow as tf
from niftynet.layer.squeeze_excitation_layer import SELayer

class SETest(tf.test.TestCase):
    def test_3d_se_shape(self):
        input_shape = (2, 16, 16, 16, 32)
        x = tf.ones(input_shape)
        se_layer = SELayer()
        out_se = se_layer(x)

        with self.test_session() as sess:
            sess.run(tf.global_variables_initializer())
            out = sess.run(out_se)
            x_shape = tuple(x.shape.as_list())
            self.assertAllClose(x_shape, out.shape)

    def test_2d_se_shape(self):
        input_shape = (2, 16, 16, 32)
        x = tf.ones(input_shape)
        se_layer = SELayer()
        out_se = se_layer(x)

        with self.test_session() as sess:
            sess.run(tf.global_variables_initializer())
            out = sess.run(out_se)
            x_shape = tuple(x.shape.as_list())
            self.assertAllClose(x_shape, out.shape)

    def test_3d_se_excitation_op(self):
        input_shape = (2, 16, 16, 16, 32)
        x = tf.random_uniform(input_shape,seed=0)
        se_layer = SELayer()
        out_se = se_layer(x)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            x=sess.run(x)
            x_0_0=float(x[0,0,0,0,0])
            x_1_0=float(x[0,1,0,0,0])
            x_0_1=float(x[0,0,0,0,1])
            x_1_1=float(x[0,1,0,0,1])

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            out = sess.run(out_se)
            out_0_0=float(out[0,0,0,0,0])
            out_1_0=float(out[0,1,0,0,0])
            out_0_1=float(out[0,0,0,0,1])
            out_1_1=float(out[0,1,0,0,1])

        div_0_0=out_0_0/x_0_0
        div_1_0=out_1_0/x_1_0
        div_0_1=out_0_1/x_0_1
        div_1_1=out_1_1/x_1_1

        with self.test_session() as sess:
            self.assertAlmostEqual(div_0_0, div_1_0)
            self.assertAlmostEqual(div_0_1, div_1_1)

    def test_2d_se_excitation_op(self):
        input_shape = (2, 16, 16, 32)
        x = tf.random_uniform(input_shape,seed=0)
        se_layer = SELayer()
        out_se = se_layer(x)

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            x=sess.run(x)
            x_0_0=float(x[0,0,0,0])
            x_1_0=float(x[0,1,0,0])
            x_0_1=float(x[0,0,0,1])
            x_1_1=float(x[0,1,0,1])

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            out = sess.run(out_se)
            out_0_0=float(out[0,0,0,0])
            out_1_0=float(out[0,1,0,0])
            out_0_1=float(out[0,0,0,1])
            out_1_1=float(out[0,1,0,1])

        div_0_0=out_0_0/x_0_0
        div_1_0=out_1_0/x_1_0
        div_0_1=out_0_1/x_0_1
        div_1_1=out_1_1/x_1_1

        with self.test_session() as sess:
            self.assertAlmostEqual(div_0_0, div_1_0)
            self.assertAlmostEqual(div_0_1, div_1_1)

    def test_pooling_op_error(self):
            with self.test_session() as sess:
                sess.run(tf.global_variables_initializer())

                with self.assertRaises(ValueError):
                    SELayer(func='ABC')

    def test_reduction_ratio_error(self):
        input_shape = (2, 16, 16, 16, 33)
        x = tf.ones(input_shape)
        se_layer = SELayer()

        with self.assertRaises(ValueError):
            se_layer(x)

if __name__ == "__main__":
    tf.test.main()