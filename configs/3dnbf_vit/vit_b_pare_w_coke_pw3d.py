_base_ = ['../_base_/default_runtime.py']
# load_from = 'exp/neuralsmpl_pare_spininit_eftcoco/epoch_45.pth'
# resume_from = 'exp/neuralsmpl_pare_stage2/epoch_1.pth'
# load_from = 'exp/neuralsmpl_voge_pare/epoch_100.pth'
# load_from = 'data/pretrained/pare_official.pth'
load_from = 'data/pretrained/vitpose-h-multi-4dhuman.pth'
#ading7/3DNBF/data/pretrained/vitpose-h-multi-4dhuman.pth
#data/pretrained/res50_coco_384x288-e6f795e9_20200709.pt
use_adversarial_train = True
find_unused_parameters = True # Debug
checkpoint_config = dict(interval=5)

# evaluate
evaluation = dict(metric=['pa-mpjpe', 'mpjpe'], eval_saved_results=False) #

#img_res = 224
img_res = 320
downsample_rate = 4
d_feature = 128
n_orient = 3
n_vert = 858
num_noise = 10
max_group = 216
num_neg = num_noise * max_group

loss_weight = 60.0
workflow = [('train', 1)]
phase = 'train' #'train'
SMPL = dict(
    DATA_DIR = 'data',
    NUM_BODY_JOINTS = 23,
    MEAN_PARAMS='data/body_models/smpl_mean_params.npz',
    MODEL_PATH='data/body_models/smpl',
    JOINT_REGRESSOR_EXTRA ='data/body_models/J_regressor_extra.npy',
    GENDER = "neutral"
)
hparams = dict(
            DATASET=dict(
                DATASETS_AND_RATIOS='h36m_mpii_lspet_coco_mpi-inf-3dhp_0.35_0.05_0.05_0.2_0.35',
                FOCAL_LENGTH=5000.0, 
                IMG_RES=img_res,
                test_indices=None,
                eval_visible_joints=True,
                # occ_info_file='exp/neuralsmpl_pare_stage2_reproduce1/3dpw_test_ds30_occ80stride10_pare_r50_grid/result_occ_info_mpjpe.json',
                # occ_info_file='exp/pare/3dpw_test_ds30_occ80stride10_pare_r50_grid/result_occ_info_mpjpe.json',
                # pred_initialization='exp/pare/3dpw_test_ds30_occ80stride10_pare_r50/result_keypoints.json',
                # saved_partseg='exp/pare/3dpw_test_ds30_occ80stride10_pare_r50/result_pred_segm_mask',

                # saved_partseg='exp/pare/3dpw_test_ds30_occ40stride10_pare_r50/result_pred_segm_mask',
                # saved_partseg='exp/pare/3dpw_test_w_kp2d_ds30_op/result_pred_segm_mask', 
                # saved_partseg='exp/pare/3doh50k_reproduce/result_pred_segm_mask', 
                # pred_initialization='exp/pare/3dpw_test_ds30/result_keypoints.json'
                # pred_initialization='exp/pare/3doh50k_reproduce/result_keypoints.json'
                ),
            MODEL=dict(
                RENDERER_PRED=dict(
                    SIGMA=1e-3,
                    GAMMA=1e-2,
                    FACES_PER_PIXEL=40,
                    RENDER_RES=img_res//4),
                RENDERER_GT=dict(
                    SIGMA=0,
                    GAMMA=1e-2,
                    FACES_PER_PIXEL=1,
                    RENDER_RES=img_res//4),
                # LOSS_WEIGHT=60.0,
                N_ORIENT=n_orient, 
                downsample_rate=downsample_rate,
                VOGE_SAMPLE=True,
            ),
            REGISTRANT=dict(
                SIGMA=1e-3,
                GAMMA=1e-2,
                FACES_PER_PIXEL=10,
                RENDER_RES=img_res//downsample_rate,
                downsample_rate=downsample_rate,
                n_orient=n_orient,
                n_vert=n_vert,
                theta=10,
                FOCAL_LENGTH=5000.0,
                IMG_RES=img_res,
                disable_occ=True, #, #True, #False,
                show_debug_info=False,
                thr_detected_joints=7,
                thr_openpose_conf=0.2,
                thr_vert_det=0.1,
                use_other_init=False,
                use_saved_coke=False,
                use_saved_partseg=False,
                use_otf_openpose=True, # True for 3dpw-AdvOcc
                use_gt_smpl=False,
                optimize_twoside=True,
                debug_feature_map=False,
                fit_z=False, #False,
                noise_100=False,
                noise_90=False,
                RUN_VISUALIZER=False,
                # mixture_path='exp/3dnbf/3dpw_test_ds30_occ80stride10_pare_r50_multihypo_nopartseg_disableocc_blendbg_fixblackbg/bg_feats_mixture_vmfsoft_nc15_2x.npy',
                # mixture_path='exp/3dnbf/3dpw_test_ds30_occ80stride10_pare_r50_multihypo_nopartseg_disableocc_blendbg_fixblackbg/bg_feats_mixture_gmm_nc15_km++_2x.npy',
                # mixture_path='exp/3dnbf/3dpw_test_ds30_occ80stride10_pare_r50_multihypo_nopartseg_reproduce/bg_feats_mixture_gmm_nc15_km++_2x.npy',
                # mixture_path='exp/3dnbf/3dpw_test_ds30_occ80stride10_pare_r50_multihypo_nopartseg_aug_noisesamplebb/bg_feats_mixture_gmm_nc15_km++_2x.npy'
                ),
            VISUALIZER=dict(
                IMG_RES=512
            ),
            DEBUG=dict(
                # save_dir='exp/3dnbf/3dpw_test_ds30_occ80stride10_pare_r50_multihypo_nopartseg_disableocc_blendbg_fixblackbg_noiseinbb_kpdrop_trainimg_gt/activation_vis/epoch_5',
                # save_dir='vmf_soft_nc15_2x',
                save_dir='gmm_nc15_km++_2x_mixture9',
                save_dir_vis='gmm_nc15_km++_2x_cmp_vis',
                # '3dnbf_resnet_bgrand_rmblk_occ80str10_dfeat64_0_epoch100.png'
                eval_occ_seg=False,
                DEBUG_LOG_DIR='debug_log',
            ),
            mesh_sample_param_path='data/sample_params/uniform/sample_data_8-2021-04-05.npz',
            renderer_type='VoGE',
            disable_inference_loss=False,
            cumulative_iters=2,
        )

body_model = dict(
    type='SMPL',
    keypoint_src='smpl_54',
    keypoint_dst='smpl_49',
    keypoint_approximate=True,
    model_path='data/body_models/smpl',
    extra_joints_regressor='data/body_models/J_regressor_extra.npy')

registrant = dict(
    type='NeuralSMPLFittingVoGE',
    body_model=dict(
        type='SMPL',
        keypoint_src='smpl_54',
        keypoint_dst='smpl_49',
        keypoint_approximate=True,
        model_path='data/body_models/smpl',
        extra_joints_regressor='data/body_models/J_regressor_extra.npy'),
    num_epochs=0 if hparams['REGISTRANT']['use_gt_smpl'] else 1,
    img_res=img_res,
    stages=[
        # dict(
        # num_iter=40,
        # fit_global_orient=True,
        # fit_transl=True,
        # fit_body_pose=False,
        # fit_betas=False,
        # keypoints3d_weight=0.0,
        # likelihood_weight=0.0,
        # keypoints2d_weight=1.0e-2,
        # segm_mask_loss_weight=0.0,
        # vertices2d_weight=0.0,
        # pose_prior_weight=0.0,
        # joint_prior_weight=0.0,
        # joint_weights=dict(
        #     body_weight=5.0,
        #     use_shoulder_hip_only=True,
        # )),
        # dict(
        #     num_iter=80,
        #     fit_global_orient=True,
        #     fit_transl=True,
        #     fit_body_pose=True,
        #     fit_betas=False,
        #     keypoints3d_weight=0*1e-2,
        #     likelihood_weight=0.0,
        #     keypoints2d_weight=1.0e-2,
        #     segm_mask_loss_weight=1*1.0,
        #     pose_prior_weight=1*5e-4,
        #     joint_prior_weight=0*1.0,
        #     vertices2d_weight=0.0,
        #     ),
        dict(
            num_iter=40,
            fit_global_orient=True,
            fit_transl=True,
            fit_body_pose=False,
            fit_betas=False,
            likelihood_weight=1.0,
            ),
        dict(
            num_iter=80,
            fit_global_orient=True,
            fit_transl=False,
            fit_body_pose=True,
            fit_betas=True,
            ),
        dict(
            num_iter=20,
            fit_global_orient=False,
            fit_transl=False,
            fit_body_pose=False,
            fit_betas=True,
            silhouette_loss_weight=1.0)
    ],
    # optimizer=dict(type='Adam', lr=0.1, betas=(0.9, 0.99)),
    optimizer=dict(type='Adam', lr=0.02, betas=(0.9, 0.99)),
    keypoints2d_loss=dict(
        type='KeypointMSELoss', loss_weight=1e-2, reduction='sum', sigma=100),
    vertices2d_loss=dict(
        type='KeypointMSELoss', loss_weight=1e-3, reduction='sum', sigma=100),
    # shape_prior_loss=dict(
    #     type='ShapePriorLoss', loss_weight=1e-1, reduction='sum'),
    joint_prior_loss=dict(
        type='JointPriorLoss', loss_weight=1e-1, reduction='sum'),
    # pose_prior_loss=dict(
    #     type='MaxMixturePrior',
    #     prior_folder='data',
    #     num_gaussians=8,
    #     loss_weight=1e-1,
    #     reduction='sum'),
    pose_prior_loss=dict(
        type='VAEPosePrior',
        prior_folder='data',
        loss_weight=1*5e-4,
        reduction='sum'),
    likelihood_loss=dict(
        type='LikelihoodLoss',
        loss_weight=1.0,
        reduction='sum',
    ),
    segm_mask_loss=dict(
        type='CrossEntropyLoss',
        loss_weight=0*1.0,
        reduction='sum'
    ),
    # silhouette_loss=dict(
    #     type='BCELoss',
    #     loss_weight=0*1.0,
    #     reduction='sum'
    # ),
    keypoints3d_loss=dict(
        type='KeypointMSELoss', loss_weight=0*1e-2, reduction='sum', sigma=100),
    # # loss_smpl_pose=dict(type='MSELoss', loss_weight=60.0),
    # # loss_smpl_betas=dict(type='MSELoss', loss_weight=0.06),
    # # loss_camera=dict(type='CameraPriorLoss', loss_weight=60.0),
    # ignore_keypoints=[
    #     'neck_openpose', 'right_hip_openpose', 'left_hip_openpose',
    #     'right_hip_extra', 'left_hip_extra',
    #     'right_shoulder_openpose', 'left_shoulder_openpose', 'pelvis_openpose',
    #     'left_bigtoe_openpose',
    #     'left_smalltoe_openpose',
    #     'left_heel_openpose',
    #     'right_bigtoe_openpose',
    #     'right_smalltoe_openpose',
    #     'right_heel_openpose',
    # ],

    ignore_keypoints=[
        # # 'neck_openpose', 'right_hip_openpose', 'left_hip_openpose',
        # # 'right_hip_extra', 'left_hip_extra',
        # # 'right_shoulder_openpose', 'left_shoulder_openpose', 'pelvis_openpose',
        # 'left_bigtoe_openpose',
        # 'left_smalltoe_openpose',
        # # 'left_heel_openpose',
        # 'right_bigtoe_openpose',
        # 'right_smalltoe_openpose',
        # # 'right_heel_openpose',
    ],


    camera=dict(
        type='PerspectiveCameras',
        convention='opencv',
        in_ndc=False,
        focal_length=5000,
        image_size=(img_res, img_res),
        principal_point=(112.0, 112.0)),
    hparams=hparams['REGISTRANT'],
    )

# optimizer
optimizer = dict(
    backbone=dict(type='Adam', lr=2e-4), head=dict(type='Adam', lr=2e-4))
optimizer_config = dict(grad_clip=None)
# optimizer_config = dict(type="GradientCumulativeOptimizerHook", cumulative_iters=2)
# learning policy
lr_config = dict(policy='step', gamma=0.1, step=[400])
runner = dict(type='EpochBasedRunner', max_epochs=300)

log_config = dict(
    interval=50,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='')
        dict(type='TensorboardLoggerHook', interval=10)
    ])

# model settings
model = dict(
    type='ImageVoGEBodyModelEstimatorSE',
    backbone=dict(
        type='ViT',
        img_size=(img_res, img_res),
        patch_size=16,#16,
        embed_dim=1280,#768,
        depth=12,
        num_heads=12,
        ratio=1,
        use_checkpoint=False,
        mlp_ratio=4,
        qkv_bias=True,
        drop_path_rate=0.3,
    ),
    head = dict(
        type = "transformer_decoder",
        IN_CHANNELS = 2048,
        TRANSFORMER_DECODER = dict(
            depth = 6,
            heads = 8,
            mlp_dim = 1024,
            dim_head = 64,
            dropout = 0.0,
            emb_dropout = 0.0,
            norm = "layer",
            context_dim = 1280,
        ),
        SMPL = SMPL,
        #IN_CHANNELS = 2048,
        # TRANSFORMER_DECODER = dict(
        #     depth = 6,
        #     heads = 8,
        #     mlp_dim = 1024,
        #     dim_head = 64,
        #     dropout = 0.0,
        #     emb_dropout = 0.0,
        #     norm = "layer",
        #     context_dim = 1280,
        # ),
        
    ),
    # head=dict(
    #     type='PareHeadwCoKe',
    #     num_joints=24, 
    #     num_input_features=2048,
    #     use_heatmaps='part_segm',
    #     smpl_mean_params='data/body_models/smpl_mean_params.npz',
    #     coke_cfg=dict(
    #     type='CoKeHead', #'CoKeHeadMultiScale', 
    #     d_coke_feat=d_feature, ),
    #     ),
    body_model_train=body_model,
    body_model_test=dict(
        type='SMPL',
        keypoint_src='h36m',
        keypoint_dst='h36m',
        model_path='data/body_models/smpl',
        joints_regressor='data/body_models/J_regressor_h36m.npy'),
    registrant=None if phase == 'train' else registrant,
    convention='smpl_49',
    feature_bank=dict(
        type='Nearest3DMemoryManager',
        inputSize=d_feature,
        outputSize=n_vert*n_orient+num_neg,
        K=1,
        num_noise=num_noise,
        num_pos=n_vert,
        num_orient=n_orient,
        momentum=0.9,
        feat_normalization=True,
    ),
    loss_contrastive=dict(type='CoKeLoss', 
                            loss_contrastive_weight=1.0,
                            loss_noise_reg_weight=1.0,
                            n_noise_points=num_noise,
                            num_neg=num_neg,
                            weight_noise=5e-3,
                            n_orient=n_orient,
                            feat_normalization=True,
                            local_size=1,
                            T=0.07,),
    # loss_keypoints3d=dict(type='SmoothL1Loss', loss_weight=100),
    # loss_keypoints2d=dict(type='SmoothL1Loss', loss_weight=10),
    loss_keypoints3d=dict(type='MSELoss', loss_weight=5*loss_weight),
    loss_keypoints2d=dict(type='MSELoss', loss_weight=5*loss_weight),
    # loss_vertex=dict(type='L1Loss', loss_weight=0),
    loss_smpl_pose=dict(type='MSELoss', loss_weight=1.0*loss_weight),
    loss_smpl_betas=dict(type='MSELoss', loss_weight=0.001*loss_weight),
    loss_camera=dict(type='CameraPriorLoss', loss_weight=60.0),
    loss_segm_mask=dict(type='CrossEntropyLoss', loss_weight=1.0*loss_weight),
    # loss_part_segm=dict(type='MSELoss', loss_weight=1.0),
    # init_cfg=dict(
        # type='Pretrained', checkpoint='data/pretrained/resnet50_spin_pw3d-e1857270_20211201.pth'),
        # type='Pretrained', checkpoint='data/pretrained/spin_pretrain.pth'),
        # type='Pretrained', checkpoint='data/pretrained/pare_official.pth'),
    hparams=hparams)
# dataset settings
dataset_type = 'HumanImageDataset'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
data_keys = [
    'has_smpl', 'smpl_body_pose', 'smpl_global_orient', 'smpl_betas',
    'smpl_transl', 'keypoints2d', 'keypoints3d', 'is_flipped', 'center',
    'scale', 'rotation', 'sample_idx', 'bbox_xywh', 
    'poses_init', 'betas_init', 'cameras_init', 'pred_segm_mask',
    'occ_mask', 'has_kp3d'
]
meta_data_keys = ['dataset_name', 'img_norm_cfg', 'image_path', 'occ_size', 
                'occ_stride', 'occ_idx', 'texture_file', 'texture_crop_tl']
train_pipeline = [
    dict(type='LoadImageFromFile'),
    # dict(type='RandomChannelNoise', noise_factor=0.0),
    # dict(type='RandomHorizontalFlip', flip_prob=0.0, convention='smpl_49'),
    # dict(type='GetRandomScaleRotation', rot_factor=0, scale_factor=0.0),
    # dict(type='ExtremeCrop', crop_prob=0.3),
    dict(type='RandomChannelNoise', noise_factor=0.4),
    dict(type='RandomHorizontalFlip', flip_prob=0.5, convention='smpl_49'),
    dict(type='GetRandomScaleRotation', rot_factor=30, scale_factor=0.25),
    dict(type='SampleBGTexture', img_res=img_res, bg_root='data/dtd/train'),
    dict(type='MeshAffine', img_res=img_res),
    dict(type='AddOcclusionPatch', occ_size=40, occ_stride=20, 
                                    dtd_root='data/dtd/train', 
                                    prob=0.0, phase='train'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=data_keys),
    dict(type='Collect', keys=['img', 'have_occ', 'occ_size', 
            'occ_stride', 'occ_idx', *data_keys], 
            meta_keys=meta_data_keys)
]
data_keys.remove('is_flipped')
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='GetRandomScaleRotation', rot_factor=0, scale_factor=0),
    dict(type='SampleBGTexture', img_res=img_res, bg_root='data/dtd/train'),
    dict(type='MeshAffine', img_res=img_res),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=data_keys),
    dict(type='Collect', keys=['img', *data_keys], meta_keys=meta_data_keys)
]
test_pipeline_occ = [
    dict(type='LoadImageFromFile'),
    dict(type='GetRandomScaleRotation', rot_factor=0, scale_factor=0),
    dict(type='MeshAffine', img_res=img_res),
    dict(type='AddOcclusionPatch', occ_size=40, occ_stride=10, dtd_root='data/dtd/test'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=data_keys),
    dict(type='Collect', keys=['img', *data_keys], meta_keys=meta_data_keys)
]
occimgen_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='GetRandomScaleRotation', rot_factor=0, scale_factor=0),
    dict(type='MeshAffine', img_res=img_res),
    dict(type='AddOcclusionPatch', occ_size=40, occ_stride=10, dtd_root='data/dtd/test'),
    dict(type='Collect', keys=['img', 'center', 'scale', 'image_path'], meta_keys=[])
]
vis_pipeline_occ = [
    dict(type='LoadImageFromFile'),
    dict(type='GetRandomScaleRotation', rot_factor=0, scale_factor=0),
    dict(type='MeshAffine', img_res=hparams['VISUALIZER']['IMG_RES']),
    dict(type='AddOcclusionPatch', occ_size=40, occ_stride=10, dtd_root='data/dtd/test'),
    dict(type='Collect', keys=['img', 'center', 'scale', 'image_path'], meta_keys=[])
]
vis_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='GetRandomScaleRotation', rot_factor=0, scale_factor=0),
    dict(type='MeshAffine', img_res=hparams['VISUALIZER']['IMG_RES']),
    dict(type='Collect', keys=['img', 'center', 'scale', 'image_path'], meta_keys=[])
]
inference_pipeline = [
    dict(type='MeshAffine', img_res=img_res),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(
        type='Collect',
        keys=['img', 'sample_idx'],
        meta_keys=['image_path', 'center', 'scale', 'rotation'])
]

data = dict(
    samples_per_gpu=16 if phase == 'train' else 8, 
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
                dataset_name='coco',
                data_prefix='data',
                pipeline=train_pipeline,
                convention='smpl_49',
                ann_file='eft_coco_all.npz'),
    # test=dict(
    #     type=dataset_type,
    #     body_model=body_model,
    #     # dataset_name='h36m',
    #     dataset_name='mpi_inf_3dhp',
    #     data_prefix='data',
    #     pipeline=test_pipeline,
    #     convention='h36m',
    #     # ann_file='spin_h36m_train_reproduce.npz'
    #     # ann_file='spin_h36m_train_mosh.npz'
    #     ann_file='spin_mpi_inf_3dhp_train_new_correct.npz'
    #     ),
    val=dict(
        type=dataset_type,
        body_model=dict(
            type='GenderedSMPL',
            keypoint_src='h36m',
            keypoint_dst='h36m',
            model_path='data/body_models/smpl',
            joints_regressor='data/body_models/J_regressor_h36m.npy'),
        dataset_name='pw3d',
        data_prefix='data',
        pipeline=test_pipeline,
        ann_file='spin_pw3d_val.npz'),
    # test=dict(
    #     type=dataset_type,
    #     body_model=dict(
    #         type='GenderedSMPL',
    #         keypoint_src='h36m',
    #         keypoint_dst='h36m',
    #         model_path='data/body_models/smpl',
    #         joints_regressor='data/body_models/J_regressor_h36m.npy'),
    #     dataset_name='demo_dataset', #'pw3d',
    #     convention='smpl_49', #h36m
    #     data_prefix='data',
    #     pipeline=test_pipeline,
    #     ann_file='demo_dataset.npz', 
    #     # pw3d_test_w_kp2d_ds30_op.npz, 
    #     # pw3d_test_w_kp2d_ds30_op_occ80_pare_r50.npz, 
    #     # pw3d_test_w_kp2d_ds30_op_occ80_pare_r50_w_parereproduceinit.npz
    #     # pw3d_test_w_kp2d_ds30_op_occ80_pare_r50_w_pareinit.npz
    #     # pw3d_test_w_kp2d_ds30_op_occ40_pare_r50_w_pareinit.npz
    #     # pw3d_test_w_kp2d_ds30_op_w_pareinit.npz
    #     # pw3d_test_w_kp2d_ds30_op_w_parereproduceinit.npz
    #     hparams=hparams['DATASET'],
    #     ), # spin_pw3d_test.npz, spin_pw3d_val.npz
    # test=dict(
    #     type=dataset_type,
    #     body_model=dict(
    #         type='SMPL',
    #         keypoint_src='h36m',
    #         keypoint_dst='h36m',
    #         model_path='data/body_models/smpl',
    #         joints_regressor='data/body_models/J_regressor_h36m.npy'),
    #     dataset_name='3doh50k',
    #     convention='smpl_49',
    #     data_prefix='data',
    #     pipeline=test_pipeline,
    #     ann_file='3doh_test_w_kp2d_rendered_op_w_pareinit.npz', 
    #     # pw3d_test_w_kp2d_ds30_op.npz
    #     # pw3d_test_w_kp2d_ds30_op_occ80_pare_r50.npz
    #     # pw3d_test_w_kp2d_ds30_op_occ40_pare_r50.npz
    #     # 3doh_test_w_kp2d_op_w_pareinit.npz
    #     hparams=hparams['DATASET']),

    # test=dict(
    #     type='OccludedHumanImageDataset',
    #     orig_cfg=dict(
    #         type=dataset_type,
    #         body_model=dict(
    #             type='GenderedSMPL',
    #             keypoint_src='h36m',
    #             keypoint_dst='h36m',
    #             model_path='data/body_models/smpl',
    #             joints_regressor='data/body_models/J_regressor_h36m.npy'),
    #         dataset_name='pw3d', #'pw3d',
    #         convention='smpl_49', #h36m
    #         data_prefix='data',
    #         pipeline=test_pipeline_occ,
    #         ann_file='pw3d_test_w_kp2d_ds30_op.npz', 
    #         hparams=hparams['DATASET'],
    #         ),
    #     occ_size=80, 
    #     occ_stride=10,
    #     textures_file='../nemo_for_human_pose/occ_analysis/texture_files_pare_r50_occ80.0_stride40_pampjpe.txt',
    #     ) # spin_pw3d_test.npz, spin_pw3d_val.npz

    test=dict(
        type=dataset_type,
        body_model=dict(
            type='GenderedSMPL',
            keypoint_src='h36m',
            keypoint_dst='h36m',
            model_path='data/body_models/smpl',
            joints_regressor='data/body_models/J_regressor_h36m.npy'),
        dataset_name='pw3d',
        convention='smpl_49',
        data_prefix='data',
        pipeline=test_pipeline_occ, #vis_pipeline, #occimgen_pipeline,
        ann_file='pw3d_test_w_kp2d_ds30_op_w_pareinit.npz', 
        hparams=hparams['DATASET'],),

    # test=dict(
    #     type=dataset_type,
    #     body_model=dict(
    #         type='GenderedSMPL',
    #         keypoint_src='h36m',
    #         keypoint_dst='h36m',
    #         model_path='data/body_models/smpl',
    #         joints_regressor='data/body_models/J_regressor_h36m.npy'),
    #     dataset_name='pw3d',
    #     convention='smpl_49',
    #     data_prefix='data',
    #     pipeline=test_pipeline, #vis_pipeline, #occimgen_pipeline,
    #     ann_file='pw3d_test_w_kp2d_ds30_op_w_pareinit.npz', 
    #     hparams=hparams['DATASET'],)
    visualization=dict(
        type=dataset_type,
        body_model=dict(
            type='GenderedSMPL',
            keypoint_src='h36m',
            keypoint_dst='h36m',
            model_path='data/body_models/smpl',
            joints_regressor='data/body_models/J_regressor_h36m.npy'),
        dataset_name='pw3d',
        convention='smpl_49',
        data_prefix='data',
        pipeline=vis_pipeline, #_occ, #, #train_pipeline, #vis_pipeline, test_pipeline_occ, 
        ann_file='pw3d_test_w_kp2d_ds30_op.npz', 
        # pw3d_test_w_kp2d_ds30_op_occ80stride10_pare_r50.npz
        # pw3d_test_w_kp2d_ds30_op.npz,
        # pw3d_test_w_kp2d_ds30_op_occ80_pare_r50.npz,
        # pw3d_test_w_kp2d_ds30_op_occ80_pare_r50_w_parereproduceinit.npz
        # pw3d_test_w_kp2d_ds30_op_occ40_pare_r50_w_pareinit.npz
        # pw3d_test_w_kp2d_ds30_op_occ80_pare_r50_w_pareinit.npz
        # pw3d_test_w_kp2d_ds30_op_w_pareinit.npz
        # pw3d_test_w_kp2d_ds30_op_w_parereproduceinit.npz
        hparams=hparams['DATASET'],
        ),
)